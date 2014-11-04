// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#ifndef EXAMPLES_BITMAP_UPLOADER_BITMAP_UPLOADER_H_
#define EXAMPLES_BITMAP_UPLOADER_BITMAP_UPLOADER_H_

#include "base/callback.h"
#include "base/containers/hash_tables.h"
#include "base/memory/scoped_ptr.h"
#include "base/memory/weak_ptr.h"
#include "mojo/public/c/gles2/gles2.h"
#include "mojo/services/public/interfaces/geometry/geometry.mojom.h"
#include "mojo/services/public/interfaces/gpu/gpu.mojom.h"
#include "mojo/services/public/interfaces/surfaces/surface_id.mojom.h"
#include "mojo/services/public/interfaces/surfaces/surfaces.mojom.h"
#include "mojo/services/public/interfaces/surfaces/surfaces_service.mojom.h"

namespace mojo {
class Shell;
class View;

// BitmapUploader is useful if you want to draw a bitmap or color in a View.
class BitmapUploader : public SurfaceClient {
 public:
  explicit BitmapUploader(View* view);
  virtual ~BitmapUploader();

  void Init(Shell* shell);

  // Sets the color which is RGBA.
  void SetColor(uint32_t color);

  enum Format {
    RGBA,  // Pixel layout on Android.
    BGRA,  // Pixel layout everywhere else.
  };

  // Sets a bitmap.
  void SetBitmap(int width,
                 int height,
                 scoped_ptr<std::vector<unsigned char>> data,
                 Format format);

 private:
  void Upload();
  void OnSurfaceConnectionCreated(SurfacePtr surface, uint32_t id_namespace);
  uint32_t BindTextureForSize(const Size size);
  uint32_t TextureFormat();

  // SurfaceClient implementation.
  virtual void ReturnResources(Array<ReturnedResourcePtr> resources) override;

  View* view_;
  SurfacesServicePtr surfaces_service_;
  GpuPtr gpu_service_;
  MojoGLES2Context gles2_context_;

  Size size_;
  uint32_t color_;
  int width_;
  int height_;
  Format format_;
  scoped_ptr<std::vector<unsigned char>> bitmap_;
  SurfacePtr surface_;
  Size surface_size_;
  uint32_t next_resource_id_;
  uint32_t id_namespace_;
  SurfaceIdPtr surface_id_;
  base::hash_map<uint32_t, uint32_t> resource_to_texture_id_map_;

  base::WeakPtrFactory<BitmapUploader> weak_factory_;

  DISALLOW_COPY_AND_ASSIGN(BitmapUploader);
};

}  // namespace mojo

#endif  // EXAMPLES_BITMAP_UPLOADER_BITMAP_UPLOADER_H_

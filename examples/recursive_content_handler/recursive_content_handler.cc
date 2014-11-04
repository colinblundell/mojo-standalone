// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "base/macros.h"
#include "base/memory/scoped_ptr.h"
#include "mojo/application/application_runner_chromium.h"
#include "mojo/application/content_handler_factory.h"
#include "mojo/public/c/system/main.h"
#include "mojo/public/cpp/application/application_connection.h"
#include "mojo/public/cpp/application/application_delegate.h"
#include "mojo/public/cpp/application/application_impl.h"
#include "mojo/public/cpp/application/interface_factory_impl.h"
#include "mojo/services/public/interfaces/content_handler/content_handler.mojom.h"

namespace mojo {
namespace examples {

class RecursiveContentHandler : public ApplicationDelegate,
                                public ContentHandlerFactory::Delegate {
 public:
  RecursiveContentHandler() : content_handler_factory_(this) {}

 private:
  // Overridden from ApplicationDelegate:
  virtual bool ConfigureIncomingConnection(
      ApplicationConnection* connection) override {
    connection->AddService(&content_handler_factory_);
    return true;
  }

  // Overridden from ContentHandlerFactory::Delegate:
  virtual scoped_ptr<ContentHandlerFactory::HandledApplicationHolder>
  CreateApplication(ShellPtr shell, URLResponsePtr response) override {
    LOG(INFO) << "RecursiveContentHandler called with url: " << response->url;
    return make_handled_factory_holder(new mojo::ApplicationImpl(
        new RecursiveContentHandler(), shell.PassMessagePipe()));
  }

  ContentHandlerFactory content_handler_factory_;

  DISALLOW_COPY_AND_ASSIGN(RecursiveContentHandler);
};

}  // namespace examples
}  // namespace mojo

MojoResult MojoMain(MojoHandle shell_handle) {
  mojo::ApplicationRunnerChromium runner(
      new mojo::examples::RecursiveContentHandler());
  return runner.Run(shell_handle);
}

// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include <stdio.h>

#include "mojo/public/c/system/main.h"
#include "mojo/public/cpp/application/application_delegate.h"
#include "mojo/public/cpp/application/application_impl.h"
#include "mojo/public/cpp/application/application_runner.h"
#include "mojo/public/cpp/application/interface_factory_impl.h"
#include "mojo/services/public/interfaces/content_handler/content_handler.mojom.h"

namespace mojo {
namespace examples {

class PrintBodyApplication : public InterfaceImpl<Application> {
 public:
  PrintBodyApplication(ShellPtr shell, ScopedDataPipeConsumerHandle body)
      : shell_(shell.Pass()), body_(body.Pass()) {
    shell_.set_client(this);
  }

  virtual void Initialize(Array<String> args) override {}

  virtual void AcceptConnection(const String& requestor_url,
                                ServiceProviderPtr service_provider) override {
    printf("ContentHandler::OnConnect - requestor_url:%s - body follows\n\n",
           requestor_url.To<std::string>().c_str());
    PrintResponse(body_.Pass());
    delete this;
  }

 private:
  void PrintResponse(ScopedDataPipeConsumerHandle body) const {
    for (;;) {
      char buf[512];
      uint32_t num_bytes = sizeof(buf);
      MojoResult result = ReadDataRaw(body.get(), buf, &num_bytes,
                                      MOJO_READ_DATA_FLAG_NONE);
      if (result == MOJO_RESULT_SHOULD_WAIT) {
        Wait(body.get(),
             MOJO_HANDLE_SIGNAL_READABLE,
             MOJO_DEADLINE_INDEFINITE);
      } else if (result == MOJO_RESULT_OK) {
        if (fwrite(buf, num_bytes, 1, stdout) != 1) {
          printf("\nUnexpected error writing to file\n");
          break;
        }
      } else {
        break;
      }

      printf("\n>>> EOF <<<\n");
    }
  }

  ShellPtr shell_;
  ScopedDataPipeConsumerHandle body_;

  MOJO_DISALLOW_COPY_AND_ASSIGN(PrintBodyApplication);
};

class ContentHandlerImpl : public InterfaceImpl<ContentHandler> {
 public:
  explicit ContentHandlerImpl() {}
  virtual ~ContentHandlerImpl() {}

 private:
  virtual void StartApplication(ShellPtr shell,
                                URLResponsePtr response) override {
    // The application will delete itself after being connected to.
    new PrintBodyApplication(shell.Pass(), response->body.Pass());
  }
};

class ContentHandlerApp : public ApplicationDelegate {
 public:
  ContentHandlerApp() : content_handler_factory_() {}

  virtual void Initialize(ApplicationImpl* app) override {}

  virtual bool ConfigureIncomingConnection(
      ApplicationConnection* connection) override {
    connection->AddService(&content_handler_factory_);
    return true;
  }

 private:
  InterfaceFactoryImpl<ContentHandlerImpl> content_handler_factory_;

  MOJO_DISALLOW_COPY_AND_ASSIGN(ContentHandlerApp);
};

}  // namespace examples
}  // namespace mojo

MojoResult MojoMain(MojoHandle shell_handle) {
  mojo::ApplicationRunner runner(new mojo::examples::ContentHandlerApp);
  return runner.Run(shell_handle);
}

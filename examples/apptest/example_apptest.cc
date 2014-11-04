// Copyright 2014 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "examples/apptest/example_client_application.h"
#include "examples/apptest/example_client_impl.h"
#include "examples/apptest/example_service.mojom.h"
#include "mojo/public/cpp/application/application_impl.h"
#include "mojo/public/cpp/application/application_test_base.h"
#include "mojo/public/cpp/bindings/callback.h"
#include "mojo/public/cpp/environment/logging.h"
#include "mojo/public/cpp/system/macros.h"

namespace mojo {
namespace {

// Exemplifies ApplicationTestBase's application testing pattern.
class ExampleApplicationTest : public test::ApplicationTestBase {
 public:
  // TODO(msw): Exemplify the use of actual command line arguments.
  ExampleApplicationTest() : ApplicationTestBase(Array<String>()) {}
  ~ExampleApplicationTest() override {}

 protected:
  // ApplicationTestBase:
  ApplicationDelegate* GetApplicationDelegate() override {
    return &example_client_application_;
  }
  void SetUp() override {
    ApplicationTestBase::SetUp();
    application_impl()->ConnectToService("mojo:example_service",
                                         &example_service_);
    example_service_.set_client(&example_client_);
  }

  ExampleServicePtr example_service_;
  ExampleClientImpl example_client_;

 private:
  ExampleClientApplication example_client_application_;

  MOJO_DISALLOW_COPY_AND_ASSIGN(ExampleApplicationTest);
};

TEST_F(ExampleApplicationTest, PongClientDirectly) {
  // Test very basic standalone ExampleClient functionality.
  ExampleClientImpl example_client;
  EXPECT_EQ(0, example_client.last_pong_value());
  example_client.Pong(1);
  EXPECT_EQ(1, example_client.last_pong_value());
}

TEST_F(ExampleApplicationTest, PingServiceToPongClient) {
  // Test ExampleClient and ExampleService interaction.
  EXPECT_EQ(0, example_client_.last_pong_value());
  example_service_->Ping(1);
  EXPECT_TRUE(example_service_.WaitForIncomingMethodCall());
  EXPECT_EQ(1, example_client_.last_pong_value());
}

template <typename T>
struct SetCallback : public Callback<void()>::Runnable {
  SetCallback(T* val, T result) : val_(val), result_(result) {}
  ~SetCallback() override {}
  void Run() const override { *val_ = result_; }
  T* val_;
  T result_;
};

TEST_F(ExampleApplicationTest, RunCallbackViaService) {
  // Test ExampleService callback functionality.
  bool was_run = false;
  example_service_->RunCallback(SetCallback<bool>(&was_run, true));
  EXPECT_TRUE(example_service_.WaitForIncomingMethodCall());
  EXPECT_TRUE(was_run);
}

}  // namespace
}  // namespace mojo

defmodule EventrWeb.Router do
  use EventrWeb, :router

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/api", EventrWeb do
    pipe_through :api
  end
end

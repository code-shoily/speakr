defmodule EventrWeb.Router do
  use EventrWeb, :router
  use Pow.Phoenix.Router

  pipeline :protected do
    plug Pow.Plug.RequireAuthenticated,
      error_handler: Pow.Phoenix.PlugErrorHandler
  end

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  scope "/" do
    pipe_through :browser

    pow_routes()
  end

  scope "/", EventrWeb do
    pipe_through [:browser, :protected]

    get "/", PageController, :index
  end

  # Other scopes may use custom stacks.
  # scope "/api", EventrWeb do
  #   pipe_through :api
  # end
end

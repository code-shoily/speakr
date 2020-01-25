defmodule EventrWeb.PageController do
  use EventrWeb, :controller

  def index(conn, _params) do
    render(conn, "index.html")
  end
end

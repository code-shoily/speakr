defmodule Eventr.Repo do
  use Ecto.Repo,
    otp_app: :eventr,
    adapter: Ecto.Adapters.Postgres
end

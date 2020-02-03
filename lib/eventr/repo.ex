defmodule Speakr.Repo do
  use Ecto.Repo,
    otp_app: :speakr,
    adapter: Ecto.Adapters.Postgres
end

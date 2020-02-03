# This file is responsible for configuring your application
# and its dependencies with the aid of the Mix.Config module.
#
# This configuration file is loaded before any dependency and
# is restricted to this project.

# General application configuration
use Mix.Config

config :speakr,
  ecto_repos: [Speakr.Repo],
  generators: [binary_id: true]

config :speakr, :pow,
  user: Speakr.Auth.User,
  repo: Speakr.Repo,
  web_module: SpeakrWeb,
  extensions: [PowResetPassword, PowEmailConfirmation],
  mailer_backend: SpeakrWeb.PowMailer,
  controller_callbacks: Pow.Extension.Phoenix.ControllerCallbacks

# Configures the endpoint
config :speakr, SpeakrWeb.Endpoint,
  url: [host: "localhost"],
  secret_key_base: "3ZMcdBo0bze/rycj10ZamgkBzJm5KtrznbTldp1lZ8qAgvx00vKMEbL6g+aK1PPH",
  render_errors: [view: SpeakrWeb.ErrorView, accepts: ~w(html json)],
  pubsub: [name: Speakr.PubSub, adapter: Phoenix.PubSub.PG2]

# Configures Elixir's Logger
config :logger, :console,
  format: "$time $metadata[$level] $message\n",
  metadata: [:request_id]

# Use Jason for JSON parsing in Phoenix
config :phoenix, :json_library, Jason

# Import environment specific config. This must remain at the bottom
# of this file so it overrides the configuration defined above.
import_config "#{Mix.env()}.exs"

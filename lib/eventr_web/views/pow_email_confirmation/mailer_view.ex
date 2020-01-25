defmodule EventrWeb.PowEmailConfirmation.MailerView do
  use EventrWeb, :mailer_view

  def subject(:email_confirmation, _assigns), do: "Confirm your email address"
end

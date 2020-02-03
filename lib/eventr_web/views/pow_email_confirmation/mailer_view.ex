defmodule SpeakrWeb.PowEmailConfirmation.MailerView do
  use SpeakrWeb, :mailer_view

  def subject(:email_confirmation, _assigns), do: "Confirm your email address"
end

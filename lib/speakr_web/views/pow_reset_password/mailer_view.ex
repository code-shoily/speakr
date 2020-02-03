defmodule SpeakrWeb.PowResetPassword.MailerView do
  use SpeakrWeb, :mailer_view

  def subject(:reset_password, _assigns), do: "Reset password link"
end

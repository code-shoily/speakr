defmodule EventrWeb.PowResetPassword.MailerView do
  use EventrWeb, :mailer_view

  def subject(:reset_password, _assigns), do: "Reset password link"
end

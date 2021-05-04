from datetime import date
from django.core.mail import send_mail
from rest_framework_simplejwt.authentication import JWTAuthentication


class TokenUtils(JWTAuthentication):
    def get_user_from_token(self, request):
        header = JWTAuthentication.get_header(self, request)
        raw_token = JWTAuthentication.get_raw_token(self, header)
        validated_token = JWTAuthentication.get_validated_token(self, raw_token)
        user = JWTAuthentication.get_user(self, validated_token)
        return user


def send_email_on_user_creation(data):
    today = date.today().strftime("%B %d, %Y")
    email_template = f"""
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

  </head>
  <body style="background-color:#f6f9fc;margin:0;padding:0;font-family:sans-serif;">
    <center class="main-wrapper" style="width:100%;table-layout:fixed;background-color:#f6f9fc;padding-bottom:40px;">
      <div class="webkit" style="max-width:600px;background-color:#ffffff;">
        <table class="outer" align="center" style="margin:0 auto;width:100%;max-width:600px;">
          <tr>
            <td>
              <table width="100%" style="margin-top:40px">
                <tr>
                  <td>
                    <img src="https://i.ibb.co/bbMrncL/Logo-Progressor.png" alt="logo" width="80" style="padding-left: 30px">
                  </td>
                  <td style="text-align:right">
                    <h1 style="padding-right:30px">Progressor</h1>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td>
              <table width="100%" style="margin-top:20px; color:#00a3ff">
                <tr>
                  <td style="text-align: center">
                    <h2 style="margin:0">{data['name']}</h2>
                  </td>
                </tr>
                <tr>
                  <td style="text-align:center">
                    <h2 style="margin:0">({today})</h2>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td>
              <table width="100%" style="margin-top:30px">
                <tr>
                  <td>
                    <h2 style="padding-left:30px; margin:0">GFG User Data ({data['gfg_handle']})</h2>
                  </td>
                </tr>
                <tr>
                  <td style="padding:0 30px">
                    <table width="100%" style="margin:20px auto; border-collapse: collapse">
                      <tr style="background-color:#000; color:#fff">
                        <td style="width:50%; text-align:center; padding:20px">
                          Total Questions
                        </td>
                        <td style="text-align:center">{data['total_questions']}</td>
                      </tr>
                      <tr style="background-color:#eeeeee">
                        <td style="width:50%; text-align:center; padding:15px">
                          School
                        </td>
                        <td style="text-align:center">{data['school']}</td>
                      </tr>
                      <tr>
                        <td style="width:50%; text-align:center; padding:15px">
                          Basic
                        </td>
                        <td style="text-align:center">{data['basic']}</td>
                      </tr>
                      <tr style="background-color:#eeeeee">
                        <td style="width:50%; text-align:center; padding:15px">
                          Easy
                        </td>
                        <td style="text-align:center">{data['easy']}</td>
                      </tr>
                      <tr>
                        <td style="width:50%; text-align:center; padding:15px">
                          Medium
                        </td>
                        <td style="text-align:center">{data['medium']}</td>
                      </tr>
                      <tr style="background-color:#eeeeee">
                        <td style="width:50%; text-align:center; padding:15px">
                          Hard
                        </td>
                        <td style="text-align:center">{data['hard']}</td>
                      </tr>
                      <tr style="background-color:#000; color:#fff">
                        <td style="width:50%; text-align:center; padding:20px">
                          Coding Score
                        </td>
                        <td style="text-align:center">{data['coding_score']}</td>
                      </tr>
                    </table>
                  </td>
                </tr>
                <tr>
                  <td style="text-align:center">
                    <div style="margin:25px 0">
                      <a style="
                          text-decoration:none;
                          color:#000;
                          padding:15px;
                          background-color:#56f6d0;
                          border-radius:50px;
                        " href="http://www.google.com">Go to Website</a>
                    </div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
        </table>
      </div>
    </center>
  </body>
</html>
    """
    send_mail(
        subject='Thank you for signing up!',
        message='Current Stats',
        html_message=email_template,
        from_email='noreply.progressor@gmail.com',
        recipient_list=[data['email']],
        fail_silently=False,
    )


def send_email_on_user_creation_leetcode(data):
    today = date.today().strftime("%B %d, %Y")
    email_template = f"""
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
      </head>
      <body style="background-color:#f6f9fc;margin:0;padding:0;font-family:sans-serif;">
        <center class="main-wrapper" style="width:100%;table-layout:fixed;background-color:#f6f9fc;padding-bottom:40px;">
          <div class="webkit" style="max-width:600px;background-color:#ffffff;">
            <table class="outer" align="center" style="margin:0 auto;width:100%;max-width:600px;">
              <tr>
                <td>
                  <table width="100%" style="margin-top:40px">
                    <tr>
                      <td style="width: 40%; text-align: right;">
                        <img src="https://i.ibb.co/bbMrncL/Logo-Progressor.png" alt="logo" width="80" style="margin-right: 20px;">
                      </td>
                      <td style="text-align:left">
                        <h1>Progressor</h1>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
                  <table width="100%" style="margin-top:20px; color:#00a3ff">
                    <tr>
                      <td style="text-align: center">
                        <h2 style="margin:0">{data['name']}</h2>
                      </td>
                    </tr>
                    <tr>
                      <td style="text-align:center">
                        <h2 style="margin:0">({today})</h2>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
                  <table width="100%" style="margin-top:30px">
                    <tr>
                      <td>
                        <h2 style="padding-left:30px; margin:0">Leetcode User Data ({data['leetcode_handle']})</h2>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:0 30px">
                        <table width="100%" style="margin:20px auto; border-collapse: collapse">
                          <tr style="background-color:#000; color:#fff">
                            <td style="width:50%; text-align:center; padding:20px">
                              Total Questions
                            </td>
                            <td style="text-align:center">{data['total_questions']}</td>
                          </tr>
                          <tr style="background-color:#eeeeee">
                            <td style="width:50%; text-align:center; padding:15px">
                              Easy
                            </td>
                            <td style="text-align:center">{data['easy']}</td>
                          </tr>
                          <tr>
                            <td style="width:50%; text-align:center; padding:15px">
                              Medium
                            </td>
                            <td style="text-align:center">{data['medium']}</td>
                          </tr>
                          <tr style="background-color:#eeeeee">
                            <td style="width:50%; text-align:center; padding:15px">
                              Hard
                            </td>
                            <td style="text-align:center">{data['hard']}</td>
                          </tr>
                          <tr style="background-color:#000; color:#fff">
                            <td style="width:50%; text-align:center; padding:20px">
                              Points
                            </td>
                            <td style="text-align:center">{data['points']}</td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td style="text-align:center">
                        <div style="margin:25px 0">
                          <a style="
                              text-decoration:none;
                              color:#000;
                              padding:15px;
                              background-color:#56f6d0;
                              border-radius:50px;
                            " href="http://www.google.com">Go to Website</a>
                        </div>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </div>
        </center>
      </body>
    </html>
    """

    send_mail(
        subject='Thank you for signing up!',
        message='Current Stats',
        html_message=email_template,
        from_email='noreply.progressor@gmail.com',
        recipient_list=[data['email']],
        fail_silently=False,
    )


def send_email_on_database_update(new_data, diff):
    today = date.today().strftime("%B %d, %Y")
    email_template = f"""
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html>
      <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

      </head>
      <body style="background-color:#f6f9fc;margin:0;padding:0;font-family:sans-serif;">
        <center class="main-wrapper" style="width:100%;table-layout:fixed;background-color:#f6f9fc;padding-bottom:40px;">
          <div class="webkit" style="max-width:600px;background-color:#ffffff;">
            <table class="outer" align="center" style="margin:0 auto;width:100%;max-width:600px;">
              <tr>
                <td>
                  <table width="100%" style="margin-top:40px">
                    <tr>
                      <td>
                        <img src="https://i.ibb.co/bbMrncL/Logo-Progressor.png" alt="logo" width="80" style="padding-left: 30px">
                      </td>
                      <td style="text-align:right">
                        <h1 style="padding-right:30px">Progressor</h1>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
                  <table width="100%" style="margin-top:20px; color:#00a3ff">
                    <tr>
                      <td style="text-align: center">
                        <h2 style="margin:0">{new_data['name']}</h2>
                      </td>
                    </tr>
                    <tr>
                      <td style="text-align:center">
                        <h2 style="margin:0">({today})</h2>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
              <tr>
                <td>
                  <table width="100%" style="margin-top:30px">
                    <tr>
                      <td>
                        <h2 style="padding-left:30px; margin:0">GFG User Data ({new_data['gfg_handle']})</h2>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:0 30px">
                        <table width="100%" style="margin:20px auto; border-collapse: collapse">
                          <tr style="background-color:#000; color:#fff">
                            <td style="width:50%; text-align:center; padding:20px">
                              Total Questions
                            </td>
                            <td style="text-align:center">{new_data['total_questions']} (+{diff['total_questions']})</td>
                          </tr>
                          <tr style="background-color:#eeeeee">
                            <td style="width:50%; text-align:center; padding:15px">
                              School
                            </td>
                            <td style="text-align:center">{new_data['school']} (+{diff['school']})</td>
                          </tr>
                          <tr>
                            <td style="width:50%; text-align:center; padding:15px">
                              Basic
                            </td>
                            <td style="text-align:center">{new_data['basic']} (+{diff['basic']})</td>
                          </tr>
                          <tr style="background-color:#eeeeee">
                            <td style="width:50%; text-align:center; padding:15px">
                              Easy
                            </td>
                            <td style="text-align:center">{new_data['easy']} (+{diff['easy']})</td>
                          </tr>
                          <tr>
                            <td style="width:50%; text-align:center; padding:15px">
                              Medium
                            </td>
                            <td style="text-align:center">{new_data['medium']} (+{diff['medium']})</td>
                          </tr>
                          <tr style="background-color:#eeeeee">
                            <td style="width:50%; text-align:center; padding:15px">
                              Hard
                            </td>
                            <td style="text-align:center">{new_data['hard']} (+{diff['hard']})</td>
                          </tr>
                          <tr style="background-color:#000; color:#fff">
                            <td style="width:50%; text-align:center; padding:20px">
                              Coding Score
                            </td>
                            <td style="text-align:center">{new_data['coding_score']} (+{diff['coding_score']})</td>
                          </tr>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td style="text-align:center">
                        <div style="margin:25px 0">
                          <a style="
                              text-decoration:none;
                              color:#000;
                              padding:15px;
                              background-color:#56f6d0;
                              border-radius:50px;
                            " href="http://www.google.com">Go to Website</a>
                        </div>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </div>
        </center>
      </body>
    </html>
        """
    send_mail(
        subject=f'GFG Data for - {today}',
        message='New Stats + Changes',
        html_message=email_template,
        from_email='noreply.progressor@gmail.com',
        recipient_list=[new_data['email']],
        fail_silently=False,
    )

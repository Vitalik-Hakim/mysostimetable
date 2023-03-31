import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_welcome_mail(user_email, user_name):
    sender_email = "Aremeyaw_a@soshgic.edu.gh"
    receiver_email = user_email
    password = "fmahzynphpogscbi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to Ujamaa!"
    message["From"] = "Hakim From Ujamaa Aremeyaw_a@soshgic.edu.gh"
    message["To"] = receiver_email

    name = user_name.capitalize()
    # Create the plain-text and HTML version of your message
    text = """"""
    html = f"""\
<div dir="ltr">
  <br clear="all" />
  <div><br /></div>
  <table
    class="gmail-row gmail-row-2"
    align="center"
    width="100%"
    border="0"
    cellpadding="0"
    cellspacing="0"
    role="presentation"
    style="
      color: rgb(0, 0, 0);
      font-family: 'Times New Roman';
      font-size: medium;
    "
  >
    <tbody style="box-sizing: border-box">
      <tr style="box-sizing: border-box">
        <td style="box-sizing: border-box">
          <table
            class="gmail-row-content"
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            width="720"
            style="width: 720px"
          >
            <tbody style="box-sizing: border-box">
              <tr style="box-sizing: border-box">
                <td
                  class="gmail-column gmail-column-1"
                  width="50%"
                  style="
                    box-sizing: border-box;
                    vertical-align: top;
                    border-width: 0px;
                    border-style: initial;
                    border-color: initial;
                  "
                >
                  <table
                    class="gmail-heading_block gmail-block-2"
                    width="100%"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    role="presentation"
                  >
                    <tbody style="box-sizing: border-box">
                      <tr style="box-sizing: border-box">
                        <td
                          class="gmail-pad"
                          style="
                            box-sizing: border-box;
                            width: 360px;
                            text-align: center;
                            padding-top: 5px;
                            padding-bottom: 5px;
                          "
                        >
                          <h1
                            style="
                              box-sizing: border-box;
                              margin: 0px;
                              color: rgb(85, 85, 85);
                              font-size: 23px;
                              font-family: Montserrat, 'Trebuchet MS',
                                'Lucida Grande', 'Lucida Sans Unicode',
                                'Lucida Sans', Tahoma, sans-serif;
                              line-height: 27.6px;
                              direction: ltr;
                            "
                          >
                            <span
                              class="gmail-tinyMce-placeholder"
                              style="box-sizing: border-box"
                              >Welcome to Ujamaa {name}</span
                            >
                          </h1>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
                <td
                  class="gmail-column gmail-column-2"
                  width="50%"
                  style="
                    box-sizing: border-box;
                    vertical-align: top;
                    border-width: 0px;
                    border-style: initial;
                    border-color: initial;
                  "
                >
                  <div
                    class="gmail-spacer_block"
                    style="
                      box-sizing: border-box;
                      height: 55px;
                      line-height: 5px;
                      font-size: 1px;
                    "
                  >
                     
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
  <table
    class="gmail-row gmail-row-3"
    align="center"
    width="100%"
    border="0"
    cellpadding="0"
    cellspacing="0"
    role="presentation"
    style="
      color: rgb(0, 0, 0);
      font-family: 'Times New Roman';
      font-size: medium;
    "
  >
    <tbody style="box-sizing: border-box">
      <tr style="box-sizing: border-box">
        <td style="box-sizing: border-box">
          <table
            class="gmail-row-content gmail-stack"
            align="center"
            border="0"
            cellpadding="0"
            cellspacing="0"
            role="presentation"
            width="720"
            style="background-position: 50% 0%; width: 720px"
          >
            <tbody style="box-sizing: border-box">
              <tr style="box-sizing: border-box">
                <td
                  class="gmail-column gmail-column-1"
                  width="50%"
                  style="
                    box-sizing: border-box;
                    vertical-align: top;
                    border-width: 0px;
                    border-style: initial;
                    border-color: initial;
                  "
                >
                  <table
                    class="gmail-text_block gmail-block-3"
                    width="100%"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    role="presentation"
                    style="word-break: break-word"
                  >
                    <tbody style="box-sizing: border-box">
                      <tr style="box-sizing: border-box">
                        <td
                          class="gmail-pad"
                          style="
                            box-sizing: border-box;
                            padding: 45px 25px 10px;
                          "
                        >
                          <div
                            style="
                              box-sizing: border-box;
                              font-family: sans-serif;
                            "
                          >
                            <div
                              class="gmail-"
                              style="
                                box-sizing: border-box;
                                font-size: 12px;
                                color: rgb(31, 11, 11);
                                line-height: 1.2;
                                font-family: Montserrat, 'Trebuchet MS',
                                  'Lucida Grande', 'Lucida Sans Unicode',
                                  'Lucida Sans', Tahoma, sans-serif;
                              "
                            >
                              <p
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  margin: 0px;
                                  font-size: 14px;
                                "
                              >
                                <span
                                  style="
                                    box-sizing: border-box;
                                    font-size: 38px;
                                  "
                                  ><strong style="box-sizing: border-box"
                                    ><span style="box-sizing: border-box"
                                      >We&#39;re happy</span
                                    ></strong
                                  ></span
                                >
                              </p>
                              <p
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  margin: 0px;
                                  font-size: 14px;
                                "
                              >
                                <span
                                  style="
                                    box-sizing: border-box;
                                    font-size: 38px;
                                  "
                                  ><strong style="box-sizing: border-box"
                                    ><span style="box-sizing: border-box"
                                      >you&#39;re here.</span
                                    ></strong
                                  ></span
                                >
                              </p>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <table
                    class="gmail-text_block gmail-block-4"
                    width="100%"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    role="presentation"
                    style="word-break: break-word"
                  >
                    <tbody style="box-sizing: border-box">
                      <tr style="box-sizing: border-box">
                        <td
                          class="gmail-pad"
                          style="
                            box-sizing: border-box;
                            padding: 10px 25px 25px;
                          "
                        >
                          <div
                            style="
                              box-sizing: border-box;
                              font-family: sans-serif;
                            "
                          >
                            <div
                              class="gmail-"
                              style="
                                box-sizing: border-box;
                                font-size: 12px;
                                color: rgb(57, 61, 71);
                                line-height: 1.8;
                                font-family: Montserrat, 'Trebuchet MS',
                                  'Lucida Grande', 'Lucida Sans Unicode',
                                  'Lucida Sans', Tahoma, sans-serif;
                              "
                            >
                              <p
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  margin: 0px;
                                  font-size: 14px;
                                "
                              >
                                You are one of the first people to join Ujamaa.
                              </p>
                              <p
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  margin: 0px;
                                  font-size: 14px;
                                "
                              >
                                You can order from Ujamaa and it will be
                                delivered to you instantly.
                              </p>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <table
                    class="gmail-button_block gmail-block-5"
                    width="100%"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    role="presentation"
                  >
                    <tbody style="box-sizing: border-box">
                      <tr style="box-sizing: border-box">
                        <td
                          class="gmail-pad"
                          style="
                            box-sizing: border-box;
                            padding: 10px 10px 15px 20px;
                          "
                        >
                          <div
                            class="gmail-alignment"
                            align="left"
                            style="box-sizing: border-box"
                          >
                            <div
                              style="
                                box-sizing: border-box;
                                display: inline-block;
                                color: rgb(255, 255, 255);
                                background-color: rgb(0, 208, 156);
                                border-radius: 4px;
                                width: auto;
                                border-width: 0px;
                                border-style: solid;
                                border-color: rgb(138, 59, 143);
                                padding-top: 10px;
                                padding-bottom: 10px;
                                font-family: Montserrat, 'Trebuchet MS',
                                  'Lucida Grande', 'Lucida Sans Unicode',
                                  'Lucida Sans', Tahoma, sans-serif;
                                font-size: 16px;
                                text-align: center;
                                word-break: keep-all;
                              "
                            ><a href="https://hgictuck.shop">
                              <span
                                style="
                                  box-sizing: border-box;
                                  padding-left: 50px;
                                  padding-right: 45px;
                                  display: inline-block;
                                "
                                ><span
                                  dir="ltr"
                                  style="
                                    box-sizing: border-box;
                                    word-break: break-word;
                                    line-height: 32px;
                                  "
                                  > Order Now!</span
                                ></span
                              ></a>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </td>
                <td
                  class="gmail-column gmail-column-2"
                  width="50%"
                  style="
                    box-sizing: border-box;
                    vertical-align: top;
                    border-width: 0px;
                    border-style: initial;
                    border-color: initial;
                  "
                >
                  <table
                    class="gmail-image_block gmail-block-3"
                    width="100%"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    role="presentation"
                  >
                    <tbody style="box-sizing: border-box">
                      <tr style="box-sizing: border-box">
                        <td
                          class="gmail-pad"
                          style="
                            box-sizing: border-box;
                            padding-right: 5px;
                            width: 360px;
                            padding-left: 0px;
                            padding-top: 25px;
                          "
                        >
                          <div
                            class="gmail-alignment"
                            align="center"
                            style="box-sizing: border-box; line-height: 10px"
                          >
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                  <div
                    class="gmail-spacer_block"
                    style="
                      box-sizing: border-box;
                      height: 40px;
                      line-height: 40px;
                      font-size: 1px;
                    "
                  >
                     
                  </div>
                  <div
                    class="gmail-spacer_block gmail-mobile_hide"
                    style="
                      box-sizing: border-box;
                      height: 40px;
                      line-height: 40px;
                      font-size: 1px;
                    "
                  >
                     
                  </div>
                  <div
                    class="gmail-spacer_block"
                    style="
                      box-sizing: border-box;
                      height: 5px;
                      line-height: 5px;
                      font-size: 1px;
                    "
                  >
                     
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</div>

    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def send_order_conf_mail(user_email, user_name):
    sender_email = "Aremeyaw_a@soshgic.edu.gh"
    receiver_email = user_email
    password = "fmahzynphpogscbi"

    message = MIMEMultipart("alternative")
    message["Subject"] = "You just Ordered!"
    message["From"] = "Hakim From Ujamaa Aremeyaw_a@soshgic.edu.gh"
    message["To"] = receiver_email

    name = user_name.capitalize()

    # Create the plain-text and HTML version of your message
    text = """"""
    html = f"""\
    <div dir="ltr">
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 83.1875px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-41p3"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 264.32px;
            display: table-cell;
            width: 264.32px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 83.1875px;
              width: 264.312px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 83.1875px;
                padding: 10px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <h1
                        style="
                          box-sizing: border-box;
                          line-height: 30.8px;
                          margin: 0px;
                          font-size: 22px;
                          font-weight: normal;
                        "
                      >
                        You just ordered!
                      </h1>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div
          class="gmail-u-col gmail-u-col-58p7"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 375.68px;
            display: table-cell;
            width: 375.68px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 83.1875px;
              width: 375.688px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 83.1875px;
                padding: 10px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 14px 20px 10px 10px;
                      "
                    >
                      <div style="box-sizing: border-box; line-height: 19.6px">
                        <a href="https://hgictuck.shop"
                          ><p
                            style="
                              box-sizing: border-box;
                              line-height: 19.6px;
                              margin: 0px;
                              text-align: right;
                            "
                          >
                            Ujamaa Tuckshop
                          </p></a
                        >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                            text-align: right;
                          "
                        >
                           
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container gmail-bayengage_cart_repeat"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        background-color: rgb(37, 163, 236);
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 300.781px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 300.781px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 300.781px;
                padding: 50px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <table
                        width="100%"
                        cellpadding="0"
                        cellspacing="0"
                        border="0"
                        style="
                          line-height: inherit;
                          vertical-align: top;
                          border-collapse: collapse;
                        "
                      >
                        <tbody
                          style="box-sizing: border-box; line-height: inherit"
                        >
                          <tr
                            style="
                              box-sizing: border-box;
                              line-height: inherit;
                              vertical-align: top;
                              border-collapse: collapse;
                            "
                          >
                            <td
                              align="center"
                              style="
                                box-sizing: border-box;
                                line-height: inherit;
                                vertical-align: top;
                                border-collapse: collapse;
                                padding-right: 0px;
                                padding-left: 0px;
                              "
                            >
                              <img
                                align="center"
                                border="0"
                                src="https://img.bayengage.com/assets/1641835590218-package%20(1).png"
                                alt=""
                                title=""
                                width="130.2"
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  outline: none;
                                  clear: both;
                                  border: none;
                                  height: auto;
                                  float: none;
                                  width: 109.188px;
                                  max-width: 130.2px;
                                  display: inline-block;
                                "
                              />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 20px 10px 10px;
                      "
                    >
                      <div style="box-sizing: border-box; line-height: 18.2px">
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 18.2px;
                            margin: 0px;
                            text-align: center;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 41.6px;
                              font-size: 32px;
                              color: rgb(255, 255, 255);
                              font-family: Poppins, sans-serif;
                            "
                            ><strong
                              style="
                                box-sizing: border-box;
                                line-height: inherit;
                              "
                              >We&#39;re working on your order!</strong
                            ></span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 217.156px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 217.156px;
              border-radius: 0px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 217.156px;
                padding: 20px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
                border-radius: 0px;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          color: rgb(255, 255, 255);
                        "
                      >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 22.4px;
                              font-size: 16px;
                              color: rgb(0, 0, 0);
                            "
                            >Hey {name}!,</span
                          >
                        </p>
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 22.4px;
                              font-size: 16px;
                              color: rgb(0, 0, 0);
                            "
                            >Thank you for ordering!
                            <br/>
                            <strong
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                "
                                > <a href="https://hgictuck.shop/order-history"
                              >Order details.  </a
                            > </strong> <br/>
                            We hope you loved your Ujamaa experience.</span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          color: rgb(255, 255, 255);
                        "
                      >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 19.6px;
                              color: rgb(0, 0, 0);
                            "
                            ><span
                              style="
                                box-sizing: border-box;
                                line-height: 22.4px;
                                font-size: 16px;
                              "
                              >If you didn&#39;t order these items, please cancel
                              this order at  <strong
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                "
                                > <a href="https://hgictuck.shop/order-history">Cancel Order </a></strong
                              > and we suggest you change your <strong
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                "
                                > <a href="https://hgictuck.shop/profile">password</a></strong
                              > 
                              after.</span
                            ></span
                          >
                        </p>
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 19.6px;
                              color: rgb(0, 0, 0);
                            "
                          >
                            <br /><span
                              style="
                                box-sizing: border-box;
                                line-height: 22.4px;
                                font-size: 16px;
                              "
                            >
                              Hakim - Ujamaa
                            </span></span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        background-color: rgb(236, 240, 241);
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 125.188px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 125.188px;
              border-radius: 0px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 125.188px;
                padding: 10px;
                border-width: 20px;
                border-style: solid;
                border-color: rgb(255, 255, 255);
                border-radius: 0px;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px 10px 0px;
                      "
                    >
                      <h4
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          margin: 0px;
                          font-weight: normal;
                          text-align: center;
                        "
                      >
                        <strong
                          style="box-sizing: border-box; line-height: inherit"
                          >YOUR ORDER WILL BEING DELIVERED TO YOU SOON!:</strong
                        >
                      </h4>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 6px 10px 10px;
                      "
                    >
                      <h3
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          margin: 0px;
                          font-size: 14px;
                          font-weight: normal;
                          text-align: center;
                        "
                      >
                        "UJAMAA"
                      </h3>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div><br /></div>
  -- <br />
</div>
    """.format(name)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def send_order_admins(user_email, user_name):
    sender_email = "Aremeyaw_a@soshgic.edu.gh"
    receiver_email = 'akosah-yiadom_i@soshgic.edu.gh'
    password = "fmahzynphpogscbi"
    Adminss = ["Aremeyaw_a@soshgic.edu.gh", "agyeman_n@soshgic.edu.gh",
               'vitalikhakim@gmail.com']
    message = MIMEMultipart("alternative")
    message["Subject"] = f"{user_name} just Ordered!(Test)"
    message["From"] = "Hakim From Ujamaa Aremeyaw_a@soshgic.edu.gh"
    message["To"] = ", ".join(Adminss)

    name = user_name.capitalize()

    # Create the plain-text and HTML version of your message
    text = """"""
    html = f"""\
    <div dir="ltr">
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 83.1875px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-41p3"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 264.32px;
            display: table-cell;
            width: 264.32px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 83.1875px;
              width: 264.312px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 83.1875px;
                padding: 10px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <h1
                        style="
                          box-sizing: border-box;
                          line-height: 30.8px;
                          margin: 0px;
                          font-size: 22px;
                          font-weight: normal;
                        "
                      >
                        {name} just ordered!
                      </h1>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div
          class="gmail-u-col gmail-u-col-58p7"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 375.68px;
            display: table-cell;
            width: 375.68px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 83.1875px;
              width: 375.688px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 83.1875px;
                padding: 10px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 14px 20px 10px 10px;
                      "
                    >
                      <div style="box-sizing: border-box; line-height: 19.6px">
                        <a href="https://hgictuck.shop"
                          ><p
                            style="
                              box-sizing: border-box;
                              line-height: 19.6px;
                              margin: 0px;
                              text-align: right;
                            "
                          >
                            Ujamaa Tuckshop
                          </p></a
                        >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                            text-align: right;
                          "
                        >
                           
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container gmail-bayengage_cart_repeat"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        background-color: rgb(37, 163, 236);
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 300.781px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 300.781px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 300.781px;
                padding: 50px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <table
                        width="100%"
                        cellpadding="0"
                        cellspacing="0"
                        border="0"
                        style="
                          line-height: inherit;
                          vertical-align: top;
                          border-collapse: collapse;
                        "
                      >
                        <tbody
                          style="box-sizing: border-box; line-height: inherit"
                        >
                          <tr
                            style="
                              box-sizing: border-box;
                              line-height: inherit;
                              vertical-align: top;
                              border-collapse: collapse;
                            "
                          >
                            <td
                              align="center"
                              style="
                                box-sizing: border-box;
                                line-height: inherit;
                                vertical-align: top;
                                border-collapse: collapse;
                                padding-right: 0px;
                                padding-left: 0px;
                              "
                            >
                              <img
                                align="center"
                                border="0"
                                src="https://img.bayengage.com/assets/1641835590218-package%20(1).png"
                                alt=""
                                title=""
                                width="130.2"
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                  outline: none;
                                  clear: both;
                                  border: none;
                                  height: auto;
                                  float: none;
                                  width: 109.188px;
                                  max-width: 130.2px;
                                  display: inline-block;
                                "
                              />
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 20px 10px 10px;
                      "
                    >
                      <div style="box-sizing: border-box; line-height: 18.2px">
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 18.2px;
                            margin: 0px;
                            text-align: center;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 41.6px;
                              font-size: 32px;
                              color: rgb(255, 255, 255);
                              font-family: Poppins, sans-serif;
                            "
                            ><strong
                              style="
                                box-sizing: border-box;
                                line-height: inherit;
                              "
                              >{name} just ordered something, Please Check ujamaa rn</strong
                            ></span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 217.156px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 217.156px;
              border-radius: 0px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 217.156px;
                padding: 20px;
                border-width: 0px;
                border-style: solid;
                border-color: transparent;
                border-radius: 0px;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          color: rgb(255, 255, 255);
                        "
                      >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 22.4px;
                              font-size: 16px;
                              color: rgb(0, 0, 0);
                            "
                            >Hello Admins!!,</span
                          >
                        </p>
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 22.4px;
                              font-size: 16px;
                              color: rgb(0, 0, 0);
                            "
                            >Someone just ordered something
                            <br/>
                            <strong
                                style="
                                  box-sizing: border-box;
                                  line-height: inherit;
                                "
                                > <a href="https://hgictuck.shop/admin/orders"
                              >Order details.  </a
                            > </strong> <br/>
                            Please check for further processing</span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px;
                      "
                    >
                      <div
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          color: rgb(255, 255, 255);
                        "
                      >
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                        </p>
                        <p
                          style="
                            box-sizing: border-box;
                            line-height: 19.6px;
                            margin: 0px;
                          "
                        >
                          <span
                            style="
                              box-sizing: border-box;
                              line-height: 19.6px;
                              color: rgb(0, 0, 0);
                            "
                          >
                            <br /><span
                              style="
                                box-sizing: border-box;
                                line-height: 22.4px;
                                font-size: 16px;
                              "
                            >
                              Ujamaa
                            </span></span
                          >
                        </p>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="gmail-u-row-container"
    style="
      box-sizing: border-box;
      line-height: inherit;
      color: rgb(0, 0, 0);
      font-family: Roboto, sans-serif;
      font-size: 14px;
      text-align: center;
      background-color: transparent;
      padding: 0px;
    "
  >
    <div
      class="gmail-u-row"
      style="
        box-sizing: border-box;
        line-height: inherit;
        margin: 0px auto;
        min-width: 320px;
        max-width: 640px;
        word-break: break-word;
        background-color: rgb(236, 240, 241);
        width: 640px;
      "
    >
      <div
        style="
          box-sizing: border-box;
          line-height: inherit;
          border-collapse: collapse;
          display: table;
          width: 640px;
          height: 125.188px;
          background-color: transparent;
        "
      >
        <div
          class="gmail-u-col gmail-u-col-100"
          style="
            box-sizing: border-box;
            line-height: inherit;
            vertical-align: top;
            max-width: 320px;
            min-width: 640px;
            display: table-cell;
            width: 640px;
          "
        >
          <div
            style="
              box-sizing: border-box;
              line-height: inherit;
              height: 125.188px;
              border-radius: 0px;
              width: 640px;
            "
          >
            <div
              style="
                box-sizing: border-box;
                line-height: inherit;
                height: 125.188px;
                padding: 10px;
                border-width: 20px;
                border-style: solid;
                border-color: rgb(255, 255, 255);
                border-radius: 0px;
              "
            >
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 10px 10px 0px;
                      "
                    >
                      <h4
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          margin: 0px;
                          font-weight: normal;
                          text-align: center;
                        "
                      >
                        <strong
                          style="box-sizing: border-box; line-height: inherit"
                          >YOUR ORDER WILL BEING DELIVERED TO YOU SOON!:</strong
                        >
                      </h4>
                    </td>
                  </tr>
                </tbody>
              </table>
              <table
                role="presentation"
                cellpadding="0"
                cellspacing="0"
                width="100%"
                border="0"
                style="
                  line-height: inherit;
                  vertical-align: top;
                  border-collapse: collapse;
                  font-family: arial, helvetica, sans-serif;
                "
              >
                <tbody style="box-sizing: border-box; line-height: inherit">
                  <tr
                    style="
                      box-sizing: border-box;
                      line-height: inherit;
                      vertical-align: top;
                      border-collapse: collapse;
                    "
                  >
                    <td
                      align="left"
                      style="
                        box-sizing: border-box;
                        line-height: inherit;
                        vertical-align: top;
                        border-collapse: collapse;
                        word-break: break-word;
                        padding: 6px 10px 10px;
                      "
                    >
                      <h3
                        style="
                          box-sizing: border-box;
                          line-height: 19.6px;
                          margin: 0px;
                          font-size: 14px;
                          font-weight: normal;
                          text-align: center;
                        "
                      >
                        "UJAMAA"
                      </h3>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div><br /></div>
  -- <br />
</div>
    """.format(name)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )

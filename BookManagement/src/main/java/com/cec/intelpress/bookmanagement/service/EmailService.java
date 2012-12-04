package com.cec.intelpress.bookmanagement.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import javax.annotation.Resource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSenderImpl;
import org.springframework.stereotype.Service;

import com.cec.intelpress.bookmanagement.domain.PdfBook;

/**
 * This is a email service used to save settings and send emails much easier
 * 
 */
@Service("emailService")
public class EmailService {

	protected static Logger logger = LoggerFactory.getLogger(EmailService.class);

	/* Email host */
	private String host = "webmail.cummingsconsultinginc.com";

	/* Server Base Address */
	private String serverAddress = "http://192.168.4.193:8080/bookmanagement/";

	/* This is our actual mail sender instance */
	private JavaMailSenderImpl sender = new JavaMailSenderImpl();
	
	@Resource(name="UserService")
	private UserService userService;
	
	/**
	 * This is called before every mail is processed so that dynamic changes to
	 * the service will affect new messages
	 */
	private void configure() {
		sender.setHost(host);
	}

	public void sendPdfEmail(PdfBook pdfBook) {
		configure();

		SimpleMailMessage message = new SimpleMailMessage();
		message.setTo(pdfBook.getEmail());
		message.setSubject("Ebook is finished!");
		message.setFrom("no-reply@cummings-inc.com");
		message.setText("This email has been sent in response to a pdf submitted to the CEC PDF Conversion system."
				+ "\n\n"
				+ "The converted file is availbile at the following location. "
				+ serverAddress + "downloadepub/" + pdfBook.getId()
				+ "\n\n"
				+ "If this is a mistake, please contact CEC at the following email: support@cummings-inc.com"
				+ "\n\n" + "Thanks!");
		sendMessage(message);
	}

	public String getHost() {
		return host;
	}

	public void setHost(String host) {
		this.host = host;
	}
	
	/**
	 * Non blocking method of sending emails, this should makes pages go ALOT faster
	 * @param message
	 */
	public void sendMessage(final SimpleMailMessage message) {
		new Thread() {
			public void start() {
				sender.send(message);
			}
		}.start();
	}

}

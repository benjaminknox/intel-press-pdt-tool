package com.cec.intelpress.bookmanagement.util;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.UnknownHostException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.List;


import org.apache.log4j.Logger;
import org.json.simple.JSONObject;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.multipart.commons.CommonsMultipartFile;

import com.cec.intelpress.bookmanagement.domain.PdfBook;
import com.cec.intelpress.bookmanagement.domain.User;
import com.cec.intelpress.bookmanagement.service.UserService;

public class Util {

	/* Development Dir*/
	public final static String UPLOADS_DIR = "src/main/webapp/uploads/";
	
	/* Production Dir*/
	//public final static String UPLOADS_DIR = "webapps/bookmanagement/uploads/";
	
	/* Development Dir*/
	public final static String PDF_DIR = "src/main/webapp/pdfs/";
	
	/* PRoduction Dir*/
	//public final static String PDF_DIR = "webapps/bookmanagement/pdfs/";
	
	public final static String RESOURCE_DIR = "";
	public final static String PDF_SERVER_LOCATION = "localhost";
	public final static int PDF_SERVER_PORT = 2000;
	private static final int PDF_SERVER_TIMEOUT = 500;
	public static final String RESET_PASSWORD = "1234";
	
	public static List<String> validArticleExtensions = Arrays.asList("pdf",
			"doc", "docx", "txt");
	protected static Logger logger = Logger
			.getLogger("Util");

	public static String sha256HashString(String stringToHash) {
		MessageDigest md;
		try {
			md = MessageDigest.getInstance("SHA-256");
			md.update(stringToHash.getBytes());

			byte byteData[] = md.digest();

			// convert the byte to hex format method 1
			StringBuffer sb = new StringBuffer();
			for (int i = 0; i < byteData.length; i++) {
				sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16)
						.substring(1));
			}

			// convert the byte to hex format method 2
			StringBuffer hexString = new StringBuffer();
			for (int i = 0; i < byteData.length; i++) {
				String hex = Integer.toHexString(0xff & byteData[i]);
				if (hex.length() == 1)
					hexString.append('0');
				hexString.append(hex);
			}
			return hexString.toString();

		} catch (NoSuchAlgorithmException e) {
			return "";
		}

	}

	/**
	 * This is check and see if the uploads dir exists, and is a folder. If the
	 * folder exists we pass on by. If the uploads directory is a file we throw
	 * an exception If it needs to be created we create it
	 * 
	 * @throws Exception
	 */
	public static void validateUploads() throws Exception {
		File uploadsDir = new File(UPLOADS_DIR);
		if (uploadsDir.exists()) {
			if (uploadsDir.isDirectory()) {
				return;
			}
			throw new Exception("Uploads Directory exists, but is a file?");
		}
		uploadsDir.mkdir();
	}

	/**
	 * This is check and see if the pdf dir exists, and is a folder. If the
	 * folder exists we pass on by. If the uploads directory is a file we throw
	 * an exception If it needs to be created we create it
	 * 
	 * @throws Exception
	 */
	public static void validatePdfs() throws Exception {
		File uploadsDir = new File(PDF_DIR);
		if (uploadsDir.exists()) {
			if (uploadsDir.isDirectory()) {
				return;
			}
			throw new Exception("Uploads Directory exists, but is a file?");
		}
		uploadsDir.mkdir();
	}

	/**
	 * This is used by controllers when they need to deal with file uploads 
	 * @param source
	 * @param destination
	 */
	public static void writeFileToFileSystem(CommonsMultipartFile source,
			File destination) {
		try {
			logger.error("Location "+destination.getAbsolutePath());
			destination.createNewFile();

			InputStream in = source.getInputStream();
			OutputStream out = new FileOutputStream(destination);
			byte buf[] = new byte[1024];
			int len;
			while ((len = in.read(buf)) > 0)
				out.write(buf, 0, len);
			out.close();
			in.close();
			logger.error("Wrote new file to ["+destination.getAbsolutePath()+"]");
		} catch (Exception e) {
			e.printStackTrace();
			logger.error("Error in writeFileToFileSystem");
		}

	}
	/**
	 * This will attempt to send a message with the supplied
	 *  information to the PDF Conversion server
	 *  
	 *  Example Message:
		{
			type : 'convert',
			in-format : 'pdf',
			out-format : 'epub',
			file-location : '/path/to/the/pdf.pdf'
		}\n
		
	 *  @param the pdf domain object to convert
	 */
	public static void sendPdfToServer(File pdf, PdfBook book) {
		JSONObject json = new JSONObject();
		json.put("type", "convert");
		json.put("in-format", "pdf");
		json.put("out-format", book.getFormat());
		json.put("file-location", pdf.getAbsolutePath());
		json.put("pdf-id", book.getId());
		OutputStream out = null;
		InputStream in = null;
		Socket requestSocket = null;
		
		try{
			//creating a socket to connect to the server
			SocketAddress sockaddr = new InetSocketAddress(PDF_SERVER_LOCATION, PDF_SERVER_PORT);
			requestSocket = new Socket();
			requestSocket.connect(sockaddr, PDF_SERVER_TIMEOUT);
			System.out.println("Connected to "+PDF_SERVER_LOCATION+" in port "+PDF_SERVER_PORT);
			
			//get Input and Output streams
			out = new BufferedOutputStream(requestSocket.getOutputStream());
			out.flush();
			in = new BufferedInputStream(requestSocket.getInputStream());
			
			//Send our PDF request to the server
			out.write(json.toJSONString().getBytes());
			out.flush();
		}
		catch(UnknownHostException unknownHost){
			System.err.println("You are trying to connect to an unknown host!");
		}
		catch(IOException ioException){
			ioException.printStackTrace();
		}
		catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * This will attempt to open a socket to the PDF server to confirm it is online
	 * @return true if the server is online
	 */
	public static boolean TestForPdfServer() {
		OutputStream out = null;
		InputStream in = null;
		Socket requestSocket = null;
		boolean returnValue = false;
		
		try{
			//creating a socket to connect to the server
			SocketAddress sockaddr = new InetSocketAddress(PDF_SERVER_LOCATION, PDF_SERVER_PORT);
			requestSocket = new Socket();
			requestSocket.connect(sockaddr, PDF_SERVER_TIMEOUT);
			System.out.println("Connected to "+PDF_SERVER_LOCATION+" in port "+PDF_SERVER_PORT);
			returnValue = true;
		}
		catch(Exception exception){
			System.err.println("You are trying to connect to an unknown host!");
		}
		return returnValue;
		
	}
	
	
}

package com.cec.intelpress.bookmanagement.util;

import java.io.File;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Arrays;
import java.util.List;

public class Util {

	public final static String UPLOADS_DIR = "src/main/webapp/uploads/";
	public final static String PDF_DIR = "src/main/webapp/pdfs/";
	public static List<String> validArticleExtensions = Arrays.asList("pdf", "doc", "docx", "txt");
	
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
	 * This is check and see if the uploads dir exists, and is a folder. 
	 * If the folder exists we pass on by.
	 * If the uploads directory is a file we throw an exception
	 * If it needs to be created we create it
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
	 * This is check and see if the pdf dir exists, and is a folder. 
	 * If the folder exists we pass on by.
	 * If the uploads directory is a file we throw an exception
	 * If it needs to be created we create it
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
}

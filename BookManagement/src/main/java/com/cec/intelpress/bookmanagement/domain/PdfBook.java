package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Table;

import org.hibernate.annotations.GenericGenerator;
import org.springframework.web.multipart.commons.CommonsMultipartFile;

@Entity
@Table(name = "pdf_books")
public class PdfBook implements Serializable {

	private static final long serialVersionUID = -5423566248002296042L;

	@Id
	@Column(name = "pdf_book_id", unique=true)
	@GeneratedValue(generator="system-uuid")
	@GenericGenerator(name="system-uuid", strategy = "uuid")
	private String id;

	@Column(name = "title")
	private String title;

	@Column(name = "author")
	private String author;

	@Column(name = "isbn")
	private String isbn;
	
	@Column(name = "pdf")
	private CommonsMultipartFile pdf;
	
	@Column(name = "pdfFileName")
	private String pdfFileName;
	
	@Column(name = "epubFileName")
	private String epubFileName;
	
	@Column(name = "mobiFileName")
	private String mobiFileName;
	
	

	public String getPdfFileName() {
		return pdfFileName;
	}

	public void setPdfFileName(String pdfFileName) {
		this.pdfFileName = pdfFileName;
	}

	public String getEpubFileName() {
		return epubFileName;
	}

	public void setEpubFileName(String epubFileName) {
		this.epubFileName = epubFileName;
	}

	public String getMobiFileName() {
		return mobiFileName;
	}

	public void setMobiFileName(String mobiFileName) {
		this.mobiFileName = mobiFileName;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}

	public CommonsMultipartFile getPdf() {
		return pdf;
	}

	public void setPdf(CommonsMultipartFile pdf) {
		this.pdf = pdf;
	}
}

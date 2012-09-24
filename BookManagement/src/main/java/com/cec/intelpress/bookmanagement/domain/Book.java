package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.OneToMany;
import javax.persistence.Table;

@Entity
@Table(name = "books")
public class Book implements Serializable {

	private static final long serialVersionUID = -5423566248002296042L;

	@Id
	@Column(name = "book_id")
	@GeneratedValue
	private Integer id;

	@Column(name = "title")
	private String title;

	@Column(name = "author")
	private String author;

	@Column(name = "publisher")
	private String publisher;

	@Column(name = "isbn")
	private String isbn;

	@Column(name = "description")
	private String description;

	@Column(name = "bookcoverurl")
	private String bookcoverurl;

	@Column(name = "buyurl")
	private String buyurl;

	@Column(name = "category")
	private String category;

	@Column(name = "suggestedreading")
	private Boolean suggestedReading;
	
	@OneToMany(fetch = FetchType.EAGER, cascade = CascadeType.ALL)
	@JoinTable(name = "book_chapters", joinColumns = { @JoinColumn(name = "book_id", nullable = false, updatable = true) }, inverseJoinColumns = { @JoinColumn(name = "chapter_id", nullable = false, updatable = true) })
	private Set<Chapter> bookChapters = new HashSet<Chapter>(0);

	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
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

	public String getPublisher() {
		return publisher;
	}

	public void setPublisher(String publisher) {
		this.publisher = publisher;
	}

	public String getIsbn() {
		return isbn;
	}

	public void setIsbn(String isbn) {
		this.isbn = isbn;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}

	public String getBookcoverurl() {
		return bookcoverurl;
	}

	public void setBookcoverurl(String bookcoverurl) {
		this.bookcoverurl = bookcoverurl;
	}

	public String getBuyurl() {
		return buyurl;
	}

	public void setBuyurl(String buyurl) {
		this.buyurl = buyurl;
	}

	public String getCategory() {
		return category;
	}

	public void setCategory(String category) {
		this.category = category;
	}

	public Set<Chapter> getBookChapters() {
		return bookChapters;
	}

	public void setBookChapters(Set<Chapter> bookChapters) {
		this.bookChapters = bookChapters;
	}

}

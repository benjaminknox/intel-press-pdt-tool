package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;

import javax.persistence.CascadeType;
import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToOne;
import javax.persistence.Table;

import org.springframework.web.multipart.commons.CommonsMultipartFile;

@Entity
@Table(name = "articles")
public class TechnicalArticle implements Serializable {

	private static final long serialVersionUID = -5423566248002296042L;

	@Id
	@Column(name = "article_id")
	@GeneratedValue
	private Integer id;

	@Column(name = "title")
	private String title;

	@Column(name = "article")
	private CommonsMultipartFile article;
	
	@Column(name = "article_name")
	private String articleName;
	
	/* The user writing the article */
	@OneToOne(cascade = CascadeType.ALL)
	private User author;
	
	@Column(name = "completed")
	private boolean completed;

	public Integer getId() {
		return id;
	}

	public CommonsMultipartFile getArticle() {
		return article;
	}

	public void setArticle(CommonsMultipartFile article) {
		this.article = article;
	}

	public User getAuthor() {
		return author;
	}

	public void setAuthor(User author) {
		this.author = author;
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

	public boolean isCompleted() {
		return completed;
	}

	public void setCompleted(boolean completed) {
		this.completed = completed;
	}

	public String getArticleName() {
		return articleName;
	}

	public void setArticleName(String articleName) {
		this.articleName = articleName;
	}

}

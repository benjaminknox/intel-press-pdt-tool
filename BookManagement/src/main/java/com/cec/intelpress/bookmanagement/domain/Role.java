package com.cec.intelpress.bookmanagement.domain;

import java.io.Serializable;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.ManyToMany;
import javax.persistence.Table;

@Entity
@Table(name = "roles")
public class Role implements Serializable {

	private static final long serialVersionUID = -5527566243002296042L;

	@Id
	@Column(name = "role_id")
	@GeneratedValue
	private Integer id;

	@Column(name = "authority")
	private String authority;

	@ManyToMany(fetch = FetchType.EAGER, mappedBy = "userRoles")
	private Set<User> users = new HashSet<User>(0);
	
	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	public Set<User> getUsers() {
		return this.users;
	}
	public String getAuthority() {
		return authority;
	}

	public void setAuthority(String authority) {
		this.authority = authority;
	}
}

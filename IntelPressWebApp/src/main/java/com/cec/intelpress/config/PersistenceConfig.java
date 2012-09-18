/*
 * Copyright (c) 2012 Cummings Engineering Consultants.  All Rights Reserved.
 *
 * This software is proprietary to, and a valuable trade secret of, Cummings
 * Engineering Consultants.
 *
 * The software and documentation may not be copied, reproduced, translated,
 * or reduced to any electronic medium or machine-readable form without a
 * prior written agreement from Cummings Engineering Consultants.
 *
 *
 * UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING, THE SOFTWARE
 * AND DOCUMENTATION ARE DISTRIBUTED ON AN "AS IS" BASIS, WITHOUT WARRANTIES
 * OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
 * PURPOSE AND NONINFRINGEMENT.  REFER TO THE WRITTEN AGREEMENT FOR SPECIFIC
 * LANGUAGE GOVERNING PERMISSIONS AND LIMITATIONS.
 */
package com.cec.intelpress.config;

import java.util.HashMap;
import java.util.Map;

import javax.sql.DataSource;

import org.apache.commons.dbcp.BasicDataSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.beans.factory.config.PropertyPlaceholderConfigurer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Profile;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;
import org.springframework.orm.jpa.JpaTransactionManager;
import org.springframework.orm.jpa.JpaVendorAdapter;
import org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean;
import org.springframework.orm.jpa.vendor.HibernateJpaVendorAdapter;
import org.springframework.transaction.PlatformTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@Configuration
@EnableTransactionManagement
public class PersistenceConfig {

	@Value("${db.dialect}")
	private String databaseDialect;

	@Value("${db.driver}")
	private String driverClassName;

	@Value("${db.url}")
	private String url;

	@Value("${db.username}")
	private String username;

	@Value("${db.password}")
	private String password;
	
	@Value("${db.hbm2ddl}")
	private String hbm2ddl;
	
	@Autowired
	private DataSource dataSource;

	@Bean
	public static PropertyPlaceholderConfigurer properties() {
		PropertyPlaceholderConfigurer ppc = new PropertyPlaceholderConfigurer();
		final Resource[] resources = new ClassPathResource[] { new ClassPathResource("db.properties") };
		ppc.setLocations(resources);
		ppc.setIgnoreUnresolvablePlaceholders(true);
		return ppc;
	}
	
	@Bean
	public JpaVendorAdapter jpaVendorAdapter() {
		final HibernateJpaVendorAdapter jpaVendorAdapter = new HibernateJpaVendorAdapter();

		jpaVendorAdapter.setDatabasePlatform(databaseDialect);
		jpaVendorAdapter.setShowSql(true);
		jpaVendorAdapter.setGenerateDdl(true);

		return jpaVendorAdapter;
	}

	@Bean
	public LocalContainerEntityManagerFactoryBean entityManagerFactory() {
		final LocalContainerEntityManagerFactoryBean entityManagerFactory = new LocalContainerEntityManagerFactoryBean();
		
		entityManagerFactory.setJpaVendorAdapter(jpaVendorAdapter());
		
		entityManagerFactory.setDataSource(dataSource);

		final Map<String, String> jpaProperties = new HashMap<String, String>();
		jpaProperties.put("hibernate.connection.charset", "UTF-8");
		jpaProperties.put("hibernate.dialect", databaseDialect);
		jpaProperties.put("hibernate.hbm2ddl.auto", hbm2ddl);
		entityManagerFactory.setJpaPropertyMap(jpaProperties);

		return entityManagerFactory;
	}

	@Bean
	public PlatformTransactionManager transactionManager() {
		final JpaTransactionManager transactionManager = new JpaTransactionManager();

		transactionManager.setEntityManagerFactory(entityManagerFactory().getObject());

		return transactionManager;
	}

	@Configuration
	@Profile("development")
	static class DevelopmentDataSource {

		@Value("${db.driver}")
		private String driverClassName;

		@Value("${db.url}")
		private String url;

		@Value("${db.username}")
		private String username;

		@Value("${db.password}")
		private String password;
		
		@Bean(destroyMethod = "close")
		public DataSource dataSource() {
			BasicDataSource dataSource = new BasicDataSource();
			dataSource.setDriverClassName(driverClassName);
			dataSource.setUrl(url);
			dataSource.setUsername(username);
			dataSource.setPassword(password);
			return dataSource;
		}
	}
	
	@Configuration
	@Profile("test")
	static class TestDataSource {

		@Value("${db.driver}")
		private String driverClassName;

		@Value("${db.url}")
		private String url;

		@Value("${db.username}")
		private String username;

		@Value("${db.password}")
		private String password;
		
		@Bean(destroyMethod = "close")
		public DataSource dataSource() {
			BasicDataSource dataSource = new BasicDataSource();
			dataSource.setDriverClassName(driverClassName);
			dataSource.setUrl(url);
			dataSource.setUsername(username);
			dataSource.setPassword(password);
			return dataSource;
		}
	}
	
	@Configuration
	@Profile("production")
	static class ProductionDataSource {

		@Value("${db.driver}")
		private String driverClassName;

		@Value("${db.url}")
		private String url;

		@Value("${db.username}")
		private String username;

		@Value("${db.password}")
		private String password;
		
		@Bean(destroyMethod = "close")
		public DataSource dataSource() {
			BasicDataSource dataSource = new BasicDataSource();
			dataSource.setDriverClassName(driverClassName);
			dataSource.setUrl(url);
			dataSource.setUsername(username);
			dataSource.setPassword(password);
			return dataSource;
		}
	}
}

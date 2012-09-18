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
package com.cec.intelpress.model.listener;

import java.util.Date;

import javax.persistence.PrePersist;
import javax.persistence.PreUpdate;

import com.cec.intelpress.model.AbstractAuditableEntity;

/**
 * Listener to set the Data when the model is persisted
 * 
 * @author joe.rawlings
 */
public class AbstractAuditableEntityListener {

	/**
	 * This is automatically run prior to saving a new entity to the data store.
	 */
	@PrePersist
	protected void prePersist(AbstractAuditableEntity entity) {
		entity.setUpdatedAt(new Date());
	}

	/**
	 * This is automatically run prior to updating an existing entity in the
	 * data store.
	 */
	@PreUpdate
	protected void preUpdate(AbstractAuditableEntity entity) {
		entity.setUpdatedAt(new Date());
	}
}

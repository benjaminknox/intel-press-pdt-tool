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
package com.cec.intelpress.dto;

import com.cec.intelpress.model.AbstractEntity;
import com.cec.intelpress.model.AbstractAuditableEntity;

import java.io.Serializable;
import java.util.Date;

import org.apache.commons.lang3.builder.ReflectionToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

/**
 * Abstract Data Transfer Object with some default attributes
 * 
 * @author joe.rawlings
 */
public abstract class AbstractDto implements Serializable {

    private static final long serialVersionUID = 3321526898957886506L;

    private long id;
    
    private Date createdAt;
    private Date updatedAt;

    /**
     * Default Constructor
     */
    protected AbstractDto() {
    }
    
    /**
     * Set the ID of this {@link AbstractDto}
     * 
     * @param id
     *            The ID to use
     */
    public AbstractDto(final long id) {
        this.setId(id);
    }

    /**
     * Convert an {@link AbstractEntity} to an {@link AbstractDto}
     * 
     * @param entity
     *            The {@link AbstractEntity} to convert
     */
    protected AbstractDto(AbstractEntity entity) {
        if (entity != null) {
            this.id = entity.getId();
            this.createdAt = entity.getCreatedAt();
        }
    }

    /**
     * Convert an {@link AbstractAuditableEntity} to an {@link AbstractDto}
     * 
     * @param entity
     *            The {@link AbstractAuditableEntity} to convert
     */
    protected AbstractDto(AbstractAuditableEntity entity) {
        if (entity != null) {
            this.id = entity.getId();
            this.createdAt = entity.getCreatedAt();
            this.updatedAt = entity.getUpdatedAt();
        }
    }

    // ////////////////////////////////////////////////////////////////
    // Getters + Setters Below
    // ////////////////////////////////////////////////////////////////

    /**
     * @return the id
     */
    public long getId() {
        return id;
    }

    /**
     * @param id
     *            the id to set
     */
    public void setId(long id) {
        this.id = id;
    }

    /**
     * @return the createdAt
     */
    public Date getCreatedAt() {
        return createdAt;
    }

    /**
     * @param createdAt
     *            the createdAt to set
     */
    public void setCreatedAt(Date createdAt) {
        this.createdAt = createdAt;
    }

    /**
     * @return the updatedAt
     */
    public Date getUpdatedAt() {
        return updatedAt;
    }

    /**
     * @param updatedAt
     *            the updatedAt to set
     */
    public void setUpdatedAt(Date updatedAt) {
        this.updatedAt = updatedAt;
    }

    /**
     * Writes the AbstractDto as a formatted String
     */
    @Override
    public String toString() {
        return (new ReflectionToStringBuilder(this, ToStringStyle.SHORT_PREFIX_STYLE)).toString();
    }
}

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
package com.cec.intelpress.model;

import java.util.Date;

import javax.persistence.Basic;
import javax.persistence.Column;
import javax.persistence.EntityListeners;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.MappedSuperclass;
import javax.persistence.Temporal;
import javax.persistence.TemporalType;
import javax.persistence.Version;

import com.cec.intelpress.model.listener.AbstractAuditableEntityListener;

/**
 * Abstract Model Entity with 'audit' features for the Todo System
 * 
 * @author joe.rawlings
 */
@MappedSuperclass
@EntityListeners({ AbstractAuditableEntityListener.class })
public abstract class AbstractAuditableEntity extends AbstractEntity {

    private static final long serialVersionUID = 1242038220068316368L;

    @Version
    @Column(name = "version", nullable = false)
    private int version;

    @Basic(optional = false)
    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "updated_at", nullable = false)
    private Date updatedAt;

    // ////////////////////////////////////////////////////////////////
    // Getters + Setters Below
    // ////////////////////////////////////////////////////////////////

    /**
     * Create a new AbstractAuditableEntity.
     */
    public AbstractAuditableEntity() {
        super();
    }

    /**
     * @return the version
     */
    public int getVersion() {
        return version;
    }

    /**
     * @param version
     *            the version to set
     */
    public void setVersion(int version) {
        this.version = version;
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
}

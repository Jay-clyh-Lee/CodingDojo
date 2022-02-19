package com.save_travels.demo.models;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;


@Entity
@Table(name="expenses")
public class Expense {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	@NotEmpty(message="This cannot be empty.")
	private String name;
	
	@NotEmpty(message="This cannot be empty.")
	private String vendor;
	
	@NotNull(message="A number is needed.")
	@Min(value=0, message="Enter a valid amount.")
	private float amount;
	
	@Size(max=1000, message="Cannot exceed 1000 characters.")
	private String description;
	
	
	// constructor
	public Expense() {}


	public Long getId() {
		return id;
	}


	public void setId(Long id) {
		this.id = id;
	}


	public String getName() {
		return name;
	}


	public void setName(String name) {
		this.name = name;
	}


	public String getVendor() {
		return vendor;
	}


	public void setVendor(String vendor) {
		this.vendor = vendor;
	}


	public float getAmount() {
		return amount;
	}


	public void setAmount(float amount) {
		this.amount = amount;
	}


	public String getDescription() {
		return description;
	}


	public void setDescription(String description) {
		this.description = description;
	}


}

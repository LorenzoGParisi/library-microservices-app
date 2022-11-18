package com.parisi.customerspring.model;

import java.util.List;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.Transient;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "customers")
public class Customer {
	@Transient
	public static final String SEQUENCE_NAME = "users_sequences";
	@Id 
	private long customerId;
	@NotBlank
	@Size(max = 50)
	private String name;
	private String surname;
	private List<Borrowing> CustomerBorrowing;
	
	public long getCustomerId() {
		return customerId;
	}
	public void setCustomerId(long customerId) {
		this.customerId = customerId;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getSurname() {
		return surname;
	}
	public void setSurname(String surname) {
		this.surname = surname;
	}
	public List<Borrowing> getCustomerBorrowing() {
		return CustomerBorrowing;
	}
	public void setCustomerBorrowing(List<Borrowing> customerBorrowing) {
		CustomerBorrowing = customerBorrowing;
	}
	@Override
	public String toString() {
		return "Customer [customerId=" + customerId + ", name=" + name + ", surname=" + surname + ", CustomerBorrowing="
				+ CustomerBorrowing + "]";
	}
}

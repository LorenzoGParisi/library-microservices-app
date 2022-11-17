package com.parisi.customerspring.model;

import java.util.List;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "CustomerDB")
public class Customer {
	
	@Id 
	private long customerId;
	@NotBlank
	@Size(max = 50)
	private String name;
	private String surname;
	
	public List<Borrowing> borrowing;
	
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
	public List<Borrowing> getBorrowing() {
		return borrowing;
	}
	public void setBorrowing(List<Borrowing> borrowing) {
		this.borrowing = borrowing;
	}
	@Override
	public String toString() {
		return "Customer [customerId=" + customerId + ", name=" + name + ", surname=" + surname + ", borrowing="
				+ borrowing + "]";
	}
}

package com.parisi.customerspring.model;

import javax.validation.constraints.NotBlank;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "books")
public class Book {
	
	@Id 
	private long bookId;
	@NotBlank
	private String title;
}

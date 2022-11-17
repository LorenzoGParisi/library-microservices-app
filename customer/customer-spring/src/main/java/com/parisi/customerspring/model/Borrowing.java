package com.parisi.customerspring.model;

import java.util.List;
import javax.validation.constraints.NotBlank;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Document(collection = "borrowings")
public class Borrowing {
	
	@Id 
	private long borrowingId;
	@NotBlank
	private List<Book> borrowingItems;
}

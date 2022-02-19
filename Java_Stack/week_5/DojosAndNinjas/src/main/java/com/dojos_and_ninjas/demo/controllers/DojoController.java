package com.dojos_and_ninjas.demo.controllers;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.dojos_and_ninjas.demo.models.Dojo;
import com.dojos_and_ninjas.demo.services.DojoService;

@Controller
public class DojoController {
	
	@Autowired
	private DojoService dojoService;
	
	@GetMapping("/")
	public String home() {
		return "redirect:/dojos"; // home page
	}
	
	// READ
	// view all dojos
	@GetMapping("/dojos")
	public String all(Model model) {
		
		model.addAttribute("dojos", dojoService.getAll());
		return "dojos.jsp"; // view all dojos page
	}
	
	// view dojo by id
	@GetMapping("/dojo/view/{id}")
	public String view(
			@PathVariable Long id,
			Model model
			) {
		
		model.addAttribute("dojo", dojoService.retrieve(id));
		
		return "showDojo.jsp";
	}
	
	// CREATE
	// add dojo page
	@GetMapping("/dojo/add")
	public String add(@ModelAttribute("dojo") Dojo dojo) {

		return "newDojo.jsp";
	}
	
	@PostMapping("/dojo/create")
	public String add(
			@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if ( result.hasErrors() ) return "home.jsp";
		
		this.dojoService.create(dojo);
		
		redirectAttributes.addFlashAttribute("message", "A new dojo has been added");
		
		return "redirect:/dojos"; 
	}
	
	// UPDATE
	// edit a dojo page  // not needed for this assignment
	@GetMapping("/dojo/edit/{id}")
	public String editDojoByIdFormPage(
			@PathVariable Long id,
			Model model
			) {
		
		model.addAttribute("dojo", dojoService.retrieve(id));
		
		return "editDojo.jsp";
	}
	
	@PostMapping("/dojo/update/{id}")
	public String update( 
			@Valid @ModelAttribute("dojo") Dojo dojo,
			BindingResult result,
			RedirectAttributes redirectAttributes
			) {
		
		if ( result.hasErrors() ) return "editDojo.jsp";
		
		this.dojoService.update(dojo); 
		
		redirectAttributes.addFlashAttribute("message", "This dojo has been updated");
		
		return String.format("redirect:/dojo/%d", dojo.getId()); // view the updated dojo
	}
	
	//DELETE
	@GetMapping("/dojo/delete/{id}")
	public String delete(
			@PathVariable Long id,
			RedirectAttributes redirectAttributes
			) {
		
		this.dojoService.delete(id);
		
		redirectAttributes.addFlashAttribute("message", "This dojo has been deleted");
		
		return "redirect:/";
	}
}

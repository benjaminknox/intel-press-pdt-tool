package com.cec.intelpress.bookmanagement.controller;

import java.io.File;
import java.util.List;
import java.util.UUID;

import javax.annotation.Resource;

import org.apache.log4j.Logger;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.multipart.commons.CommonsMultipartFile;
import org.springframework.web.servlet.ModelAndView;

import com.cec.intelpress.bookmanagement.domain.PdfBook;
import com.cec.intelpress.bookmanagement.service.PdfBookService;
import com.cec.intelpress.bookmanagement.service.UserService;
import com.cec.intelpress.bookmanagement.util.Util;

@Controller
@SessionAttributes
@RequestMapping("/admin/pdfmanagement")
@PreAuthorize("hasRole('ROLE_ADMIN')")
public class PdfManagementController {

	protected static Logger logger = Logger
			.getLogger("RoleManagementController");

	@Resource(name = "UserService")
	private UserService userService;
	@Resource(name = "PdfBookService")
	private PdfBookService pdfService;

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public ModelAndView getRoleManagement(Model model) {

		ModelAndView mav = new ModelAndView();

		List<PdfBook> allPdfs = pdfService.getAll();
		mav.addObject("pdfs", allPdfs);
		
		mav.setViewName("pdfmanagement");
		return mav;
	}
	
	@RequestMapping(value = "/delpdf/{pdfid}", method = RequestMethod.GET)
	public String delBook(@PathVariable(value = "pdfid") String pdfid) {

		pdfService.delete(pdfid);
		return "redirect:/admin/pdfmanagement/";
	}
 
	@RequestMapping(value = "/ebooks/{pdfid}", method = RequestMethod.GET)
	public ModelAndView ebooks(@PathVariable(value = "pdfid") String bookId) {
		PdfBook book = pdfService.get(bookId);
		
		ModelAndView mav = new ModelAndView();
		
		mav.setViewName("ebooks");
		mav.addObject("pdf", book);
		
		return mav;
	}
	
	@RequestMapping(value = "/uploadebook", method = RequestMethod.POST)
	public String addChapter(@RequestParam(value = "epub") CommonsMultipartFile epub, 
			@RequestParam(value = "mobi") CommonsMultipartFile mobi,
			@RequestParam(value = "pdf") String pdf) throws Exception {
		//TODO: Fix this terrible code	
		
		PdfBook pdfBook = pdfService.get(pdf);
		
		Util.validatePdfs();
		
		String[] epubName = epub.getOriginalFilename().split("\\.");
		if(epubName.length >= 2) {
			String epubUploadName = String.valueOf(UUID.randomUUID() + "." + epubName[1]);
			File epubFileName = new File(Util.UPLOADS_DIR+epubUploadName);
			try{
				epub.transferTo(epubFileName);
				pdfBook.setEpubFileName(epubUploadName);
				logger.debug("Set epub name");
			} catch(Exception e) {
				logger.error(e.getMessage());
			}
		}
		
		String[] mobiName = mobi.getOriginalFilename().split("\\.");
		if(mobiName.length >= 2) {
			String mobiUploadName = String.valueOf(UUID.randomUUID() + "." + mobiName[1]);
			File mobiFileName = new File(Util.UPLOADS_DIR+mobiUploadName);
			try{
				mobi.transferTo(mobiFileName);
				pdfBook.setMobiFileName(mobiUploadName);
				logger.debug("set mobi name");
			} catch(Exception e) {
				logger.error(e.getMessage());
			}
		}
		pdfService.edit(pdfBook);
		
		return "redirect:/admin/pdfmanagement/ebooks/"+pdf;
	}
}
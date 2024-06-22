package nl.roelofvdg.pdfsam_109;

import java.io.Serializable;

public class FileNameRequest implements Serializable {

    private static final long serialVersionUID = -4901506757147449856L;

    private Integer pageNumber = null;
    private Integer fileNumber = null;
    private String bookmarkName = null;

    /**
     * @param pageNumber
     * @param fileNumber
     * @param bookmarkName
     */
    public FileNameRequest(Integer pageNumber, Integer fileNumber, String bookmarkName) {
        super();
        this.pageNumber = pageNumber;
        this.fileNumber = fileNumber;
        this.bookmarkName = bookmarkName;
    }

    public FileNameRequest(int pageNumber, int fileNumber, String bookmarkName) {
        this(new Integer(pageNumber),new Integer(fileNumber), bookmarkName);
    }

    public FileNameRequest() {
    }

    /**
     * @return the pageNumber
     */
    public Integer getPageNumber() {
        return pageNumber;
    }

    /**
     * @param pageNumber the pageNumber to set
     */
    public void setPageNumber(Integer pageNumber) {
        this.pageNumber = pageNumber;
    }

    /**
     * @return the fileNumber
     */
    public Integer getFileNumber() {
        return fileNumber;
    }

    /**
     * @param fileNumber the fileNumber to set
     */
    public void setFileNumber(Integer fileNumber) {
        this.fileNumber = fileNumber;
    }

    /**
     * @return the bookmarkName
     */
    public String getBookmarkName() {
        return bookmarkName;
    }

    /**
     * @param bookmarkName the bookmarkName to set
     */
    public void setBookmarkName(String bookmarkName) {
        this.bookmarkName = bookmarkName;
    }

    /**
     * @return true if all the instance variables are null or empty
     */
    public boolean isEmpty(){
        return ((bookmarkName==null || bookmarkName.length()==0) && (fileNumber==null) && (pageNumber==null));
    }

}

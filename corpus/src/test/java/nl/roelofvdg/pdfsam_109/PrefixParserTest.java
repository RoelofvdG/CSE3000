package nl.roelofvdg.pdfsam_109;

import org.junit.Test;

import static org.junit.Assert.*;

public class PrefixParserTest {

    @Test
    public void testGenerateFileNameIntegerIntegerCURRENTPAGEComplexFILENUMBERComplex() {
        try {
            PrefixParser parser = new PrefixParser("[CURRENTPAGE###]_[FILENUMBER##]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(2), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "020_02_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerIntegerCURRENTPAGEComplexFILENUMBERComplexWithStart() {
        try {
            PrefixParser parser = new PrefixParser("[CURRENTPAGE###]_[FILENUMBER###25]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(2), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "020_027_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    /**
     * File number exceed the given patter
     */
    @Test
    public void testGenerateFileNameIntegerIntegerBASENAMEComplexFILENUMBERComplex() {
        try {
            PrefixParser parser = new PrefixParser("[BASENAME]_[FILENUMBER##]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(222), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "filename_222_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerIntegerCURRENTPAGEComplexFILENUMBERComplex2() {
        try {
            PrefixParser parser = new PrefixParser("[CURRENTPAGE###]_[FILENUMBER##]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(222), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "020_222_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerIntegerCURRENTPAGEComplex() {
        try {
            PrefixParser parser = new PrefixParser("[CURRENTPAGE###]_[FILENUMBER]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(1), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "020_1_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerIntegerCURRENTPAGESimple() {
        try {
            PrefixParser parser = new PrefixParser("[CURRENTPAGE]_[FILENUMBER]_test", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), new Integer(1), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "20_1_test.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerCURRENTPAGEComplex() {
        try {
            PrefixParser parser = new PrefixParser("[FILENUMBER]_test[CURRENTPAGE####]_", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), null, null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "[FILENUMBER]_test0020_.pdf", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerCURRENTPAGESimple() {
        try {
            PrefixParser parser = new PrefixParser("[FILENUMBER]_test[CURRENTPAGE]_", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), null, null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "[FILENUMBER]_test20_.pdf", actual);

        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameIntegerFILENUMBERSimpleWithStart() {
        try {
            PrefixParser parser = new PrefixParser("[FILENUMBER25]_test[CURRENTPAGE]_", "filename");
            FileNameRequest request = new FileNameRequest(null, new Integer(20), null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "45_test[CURRENTPAGE]_.pdf", actual);

        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameCURRENTPAGESimple() {
        try {
            PrefixParser parser = new PrefixParser("prefix_", "filename");
            FileNameRequest request = new FileNameRequest(new Integer(20), null, null);
            String actual = parser.generateFileName(request);
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "20_prefix_filename.pdf", actual);

        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileNameSimple() {
        try {
            PrefixParser parser = new PrefixParser("prefix_", "filename");
            String actual = parser.generateFileName();
            assertNotNull("Actual is null", actual);
            assertEquals("Actual is " + actual, "prefix_filename.pdf", actual);

        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testGenerateFileName() {
        try {
            PrefixParser parser = new PrefixParser("[TIMESTAMP]", "filename");
            String actual = parser.generateFileName();
            System.out.print(actual);
            assertNotNull("Actual is null", actual);
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

}
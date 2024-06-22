package nl.roelofvdg.summa_44;

import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.junit.Test;
import static org.junit.Assert.*;

public class DateTimeTest  {
    public static final String tOK = "2010-01-30T15:58:45+0200";
    public static final String tOK2 = "2010-12-06T15:02:45";
    public static final String tDate = "2010-01-30";
    public static final String tDefect = "200-01-30T15:58:45+0200";


    @Test
    public void testDateExpand() throws Exception {
        assertEquals("Locale en",
                "'2010-01-30 30/01-2010 01/30-2010 30/01/2010 20100130 "
                        + "30/01 01/30 01-30 30/1 1/30 1-30 January Jan'",
                "'" + DateTime.dateExpand(tOK, "en") + "'");
        assertEquals("Locale da",
                "'2010-01-30 30/01-2010 01/30-2010 30/01/2010 20100130 "
                        + "30/01 01/30 01-30 30/1 1/30 1-30 januar jan.'",
                "'" + DateTime.dateExpand(tOK, "da") + "'");
        assertEquals("Locale en part",
                "'2010-12-06 06/12-2010 12/06-2010 06/12/2010 20101206 "
                        + "06/12 12/06 12-06 6/12 12/6 12-6 December Dec'",
                "'" + DateTime.dateExpand(tOK2, "en") + "'");
        assertEquals("Locale en date only",
                "'2010-01-30 30/01-2010 01/30-2010 30/01/2010 20100130 "
                        + "30/01 01/30 01-30 30/1 1/30 1-30 January Jan'",
                "'" + DateTime.dateExpand(tDate, "en") + "'");
        assertEquals("Defect",
                tDefect, DateTime.dateExpand(tDefect, ""));
    }

    @Test
    public void testTimeExpand() throws Exception {
        assertEquals("Full", "'15:58 15.58 1558 15h58m 15:58:15 15h58m15s'",
                "'" + DateTime.timeExpand(tOK, "") + "'");
        assertEquals("Part", "'15:02 15.02 1502 15h02m 15:02:15 15h02m15s'",
                "'" + DateTime.timeExpand(tOK2, "") + "'");
        assertEquals("Defect", tDefect,
                DateTime.timeExpand(tDefect, ""));
    }

    public void testDivide() throws Exception {
        assertEquals("2010/01/30/15/58/45", DateTime.divide(tOK, 1, 100));
        assertEquals("2010/01/30/15", DateTime.divide(tOK, 1, 4));
        assertEquals("2010", DateTime.divide(tOK, 1, 1));
        assertEquals("15/58/45", DateTime.divide(tOK, 4, 6));

        assertEquals("Date", "2010/01/30", DateTime.divide(tDate, 1, 100));
        assertEquals("Defect", "", DateTime.divide(tDefect, 1, 100));
    }
}
package nl.roelofvdg.summa_44;

import org.junit.Test;

import static org.junit.Assert.*;

public class StringMapTest {

    @Test
    public void testEscape() throws Exception {
        for (String[] entry: entries) {
            assertEquals("Escape and unescape should be reflective for key",
                    entry[0],
                    StringMap.unescape(StringMap.escape(entry[0])));
            assertEquals("Escape and unescape should be reflective for value",
                    entry[1],
                    StringMap.unescape(StringMap.escape(entry[1])));
        }
    }

    // FIXME: StringMap should handle the empty key and value
    private static final String[][] entries = new String[][]{
            {"=/e/s\n///n/ee/s", "\n"},
            {"", ""},
            {"d", ""},
            {"=", "="},
            {"hello world", "!"}
    };

    @Test
    public void testFormalString() throws Exception {
        StringMap original = new StringMap(10);
        for (String[] entry: entries) {
            original.put(entry[0], entry[1]);
        }
        for (String[] entry: entries) {
            assertEquals("The original value should match",
                    entry[1], original.get(entry[0]));
        }

        String formal = original.toFormal();
        StringMap fromFormal = StringMap.fromFormal(formal);
        assertEquals("The map should survive to and from formal String",
                original, fromFormal);

        for (String[] entry: entries) {
            assertEquals("The extracted value should match",
                    entry[1], fromFormal.get(entry[0]));
        }
    }

}
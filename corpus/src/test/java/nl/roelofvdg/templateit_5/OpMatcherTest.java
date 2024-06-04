package nl.roelofvdg.templateit_5;

import org.junit.Test;

import static org.junit.Assert.*;
// INSERT IMPORTS HERE

public class OpMatcherTest {

    private final String test1 = "x = y + z";
    private final String test2 = "@template_begin(a, b) #a x = #b";

    @Test
    public void testMmatchTemplateBegin() {

        String[] testInput =
                {"\nhello \n@template_begin\n \t(\n t1\n,\np1\n,\n p2 \n,\np3) \n\n\n",
                        "@template_begin(t1,p1,p2,p3)",
                        "@template_begin(t1)",
                        "@template_begin( p1 )",
                        "@tbegin(a)",
                        "@tbegin( a , b , c )",
                        "fsdf @tbegin( a , b , c ) fsdfsda ",
                        "",
                        null,
                };
        int[] testResultCheck = {4, 4, 1, 1, 1, 3, 3, 0, 0};

        for (int i = 0; i < testResultCheck.length; i++) {
            String[] res = OpMatcher.matchTemplateBegin(testInput[i]);
            if (res == null) {
                assertEquals(0, testResultCheck[i]);
            } else {
                assertEquals(testResultCheck[i], res.length);
            }
        }

    }

    @Test
    public void testStyleMatcher() {

        String[] testInput =
                {
                        "@style( A )",
                        "@style( B )",
                        "@style( C , false )",
                        "@style( D , true )",
                        "@style( E , no )",
                };
        NamedStyle[] expectedResult =
                {
                        new NamedStyle("A", false),
                        new NamedStyle("B", false),
                        new NamedStyle("C", false),
                        new NamedStyle("D", true),
                        null,
                };

        for (int i = 0; i < testInput.length; i++) {
            NamedStyle style = OpMatcher.matchStyle(testInput[i]);
            if (style == null) {
                assertNull(expectedResult[i]);
            } else {
                assertEquals(expectedResult[i].getName(), style.getName());
                assertEquals(expectedResult[i].hasParam(), style.hasParam());
            }
        }
    }

    // INSERT TESTS HERE
}
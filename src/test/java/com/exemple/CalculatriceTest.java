package com.exemple;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class CalculatriceTest {
    private final Calculatrice c = new Calculatrice();

    @Test void addition()       { assertEquals(5, c.additionner(2, 3)); }
    @Test void multiplication() { assertEquals(20, c.multiplier(4, 5)); }
    @Test void division()       { assertEquals(2.5, c.diviser(10, 4)); }
    @Test void divisionParZero() {
        assertThrows(IllegalArgumentException.class, () -> c.diviser(1, 0));
    }
}

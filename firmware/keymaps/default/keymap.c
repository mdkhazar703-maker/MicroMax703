#include QMK_KEYBOARD_H

enum custom_keycodes {
    SCREENSHOT = SAFE_RANGE
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

    [0] = LAYOUT(
        SCREENSHOT, KC_P1, KC_P2,
        KC_P3,      KC_P4, KC_P5,
        KC_P6,      KC_P7, KC_P8
    )
};

#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [0] = {
        ENCODER_CCW_CW(KC_VOLD, KC_VOLU),
        ENCODER_CCW_CW(KC_BRID, KC_BRIU)
    }
};
#endif

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    switch (keycode) {
        case SCREENSHOT:
            if (record->event.pressed) {
                SEND_STRING(SS_DOWN(X_LGUI) SS_DOWN(X_LSFT) SS_TAP(X_S) SS_UP(X_LSFT) SS_UP(X_LGUI));
            }
            break;
    }
    return true;
}
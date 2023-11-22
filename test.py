def entferne_kommentare(text):
    in_kommentar = False
    result = []
    ignore_empty_line = False

    for char in text:
        if char == '{':
            in_kommentar = True
        elif char == '}':
            in_kommentar = False
        elif char == '\n' and not in_kommentar:
            # Setze flag, um leere Zeilen zu ignorieren
            ignore_empty_line = True
            continue
        elif not in_kommentar:
            if char != ' ' and char != '\t':
                # Wenn ein nicht-leeres Zeichen außerhalb von Kommentaren gefunden wird,
                # hebe das Flag auf, um leere Zeilen zu berücksichtigen
                ignore_empty_line = False
            result.append(char)

    # Entferne leere Zeilen, die durch das Entfernen von Kommentaren entstanden sind
    result_lines = ''.join(result).split('\n')
    filtered_lines = [line for line in result_lines if line.strip() != '' or ignore_empty_line]
    return '\n'.join(filtered_lines)

# Beispielaufruf
input_text = "FOO\n{Test}\nBAR"
assert entferne_kommentare(input_text) == "FOO\nBAR"

print("Test erfolgreich durchgeführt.")

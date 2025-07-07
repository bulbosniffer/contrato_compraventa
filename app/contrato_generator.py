from fpdf import FPDF
import tempfile

def generar_contrato(datos):
    # Oficio: 8.5 x 13 pulgadas = 216 x 330 mm
    pdf = FPDF(format=(216, 330))
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "", 11)

    # ----------------------------------------------------------
    # Encabezado
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "CONTRATO DE COMPRA VENTA DE UN TERRENO EN ESCRITURA PRIVADA", ln=True, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", "", 11)
    pdf.write(6, "CONTRATO DE COMPRA VENTA QUE SE CELEBRA EN ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["lugar"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", ESTADO DE CHIAPAS, MÉXICO, SIENDO LAS ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["hora"])

    pdf.set_font("Arial", "", 11)
    pdf.write(6, " DEL DÍA ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["fecha"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", ANTE TESTIGOS QUE DAN FE QUE FIRMAN AL CALCE DE ESTE DOCUMENTO, "
                "COMPARECIERON VOLUNTARIAMENTE POR UNA PARTE EL SR. ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["nombre_vendedor"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", QUIEN SE LE DENOMINARÁ EN ADELANTE COMO VENDEDOR, DICE TENER SU DOMICILIO EN ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["direccion_vendedor"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", Y SE IDENTIFICA CON ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["identificacion_vendedor"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", MAYOR DE EDAD EN PLENO USO DE SUS FACULTADES FÍSICAS Y MENTALES, "
                "POR SU PROPIO DERECHO VIENE A CELEBRAR EL PRESENTE CONTRATO DE COMPRA VENTA, Y DE LA OTRA PARTE EL SR. ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["nombre_comprador"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", QUIEN DENOMINAREMOS EN ADELANTE COMO EL COMPRADOR, SE IDENTIFICA CON ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["identificacion_comprador"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", CON DOMICILIO EN ")

    pdf.set_font("Arial", "B", 11)
    pdf.write(6, datos["direccion_comprador"].upper())

    pdf.set_font("Arial", "", 11)
    pdf.write(6, ", CON PLENA CAPACIDAD PARA OBLIGARSE Y CONTRATAR, HACEN CONSTAR QUE POR SUS PROPIOS DERECHOS "
                "Y EN PLENO USO DE SUS FACULTADES MENTALES, FORMALIZAN AL TENOR DE LOS ANTECEDENTES Y CLÁUSULAS SIGUIENTES.")
    pdf.ln(10)


    
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "------------------------------------------------ANTECEDENTES------------------------------------------------", ln=True, align="C")
    pdf.ln(3)

    pdf.set_font("Arial", "", 11)
    antecedentes = (
        "I.- MANIFIESTA EL VENDEDOR QUE EL CONTRATO DE COMPRA VENTA QUE HOY REALIZA LO LLEVA A CABO CON APEGO Y FUNDAMENTO LEGAL EN LOS ARTICULOS 68, 69 Y 80 DE LA LEY AGRARIA Y ORGANICA DE LOS TRIBUNALES AGRARIOS VIGENTES EN EL ESTADO Y LA FEDERACION, "
        "POR SER EL DUEÑO JUSTO Y LEGITIMO DE UN TERRENO Y QUE HOY VENDE LA PARTE DEL AREA GEOGRAFICA QUE LE CORRESPONDE Y ESTA UBICADO EN:"
    )
    pdf.multi_cell(0, 6, antecedentes, align="J")
    pdf.ln(2)

    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, datos["ubicacion_terreno"].upper(), align="J")
    pdf.ln(2)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        "SEGÚN DOCUMENTO QUE PRESENTA EN SU PODER Y QUE EXHIBE A LA VISTA, "
        "QUIEN POR ASI CONVENIR A SUS INTERESES DISGREGA UN SITIO CON LAS SIGUIENTES MEDIDAS Y COLINDANCIAS:"
    , align="J")
    pdf.ln(2)

    # Colindancias
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, f"AL NORTE: {datos['norte']}", align="J")
    pdf.multi_cell(0, 6, f"AL SUR: {datos['sur']}", align="J")
    pdf.multi_cell(0, 6, f"AL ORIENTE: {datos['oriente']}", align="J")
    pdf.multi_cell(0, 6, f"AL PONIENTE: {datos['poniente']}", align="J")
    pdf.ln(2)

    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        "II.- EL VENDEDOR MANIFIESTA QUE DICHO INMUEBLE SE ENCUENTRA AMPARADO LEGALMENTE CON DOCUMENTO DE CONTRATO DE COMPRA VENTA CELEBRADO CON EL SR. DAMAS ORTIZ LOPEZ, EL CUAL SE ANEXA AL PRESENTE DOCUMENTO Y SE ENCUENTRA LIBRE DE TODO GRAVAMEN Y RESPONSABILIDAD.\n\n"
        "III.- AMBAS PARTES MANIFIESTAN QUE LA CELEBRACION DEL PRESENTE CONTRATO SE HA REALIZADO SIN QUE HAYA EXISTIDO ERROR, DOLO, MALA FE O PRESION ALGUNA QUE PUEDA INVALIDARLO.\n\n"
    , align="J")

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 10, "--------------------------------------------------CLAUSULAS--------------------------------------------------", ln=True, align="C")
    pdf.ln(3)

    # CLAUSULAS
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, "PRIMERA:", align="J")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        " EL VENDEDOR EXPRESA QUE DE SU LIBRE Y EXPRESA VOLUNTAD VENDE, CEDE Y TRASPASA LOS DERECHOS QUE LE ASISTEN A LA PROPIEDAD SEÑALADA, "
        "CON APEGO A LO DISPUESTO POR LOS ARTICULOS 68, 69 Y 80 DE LA LEY AGRARIA.", align="J")

    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, "SEGUNDA:", align="J")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        " EL VENDEDOR VENDE LA PROPIEDAD DESCRITA CON TODOS SUS FRUTOS, ANEXOS Y COLINDANCIAS.", align="J")

    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, "TERCERA:", align="J")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        f" EL PRECIO DE LA OPERACION SE EJECUTA POR LA CANTIDAD DE ${datos['valor']} ({datos['valor_letra']}), "
        "QUE SON PAGADOS AL MOMENTO DE LA FIRMA DEL PRESENTE CONTRATO.", align="J")

    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, "CUARTA:", align="J")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        " AMBAS PARTES ACEPTAN EL CONTRATO EN TODAS SUS PARTES Y EL VENDEDOR ENTREGA LA POSESION Y DOMINIO DEL INMUEBLE.", align="J")

    pdf.ln(2)
    pdf.set_font("Arial", "B", 11)
    pdf.multi_cell(0, 6, "QUINTA:", align="J")
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6,
        " EL VENDEDOR SE COMPROMETE A RESPONDER POR EL SANEAMIENTO PARA EL CASO DE EVICCION, CONFORME AL ARTICULO 2246 DEL CODIGO CIVIL DEL ESTADO DE CHIAPAS.", align="J")

    pdf.ln(5)
    pdf.ln(10)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 6, "ATENTAMENTE", ln=1, align="C")
    pdf.ln(5)

    # Firmas principales
    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "FIRMA DE CONFORMIDAD", 0, 0, "C")
    pdf.cell(0, 6, "FIRMA DE CONFORMIDAD", 0, 1, "C")

    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "EL VENDEDOR", 0, 0, "C")
    pdf.cell(0, 6, "EL COMPRADOR", 0, 1, "C")

    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "_________________________________", 0, 0, "C")
    pdf.cell(0, 6, "_________________________________", 0, 1, "C")

    pdf.set_font("Arial", "B", 11)
    pdf.cell(90, 6, f"SR. {datos.get('nombre_vendedor', '').upper()}", 0, 0, "C")
    pdf.cell(0, 6, f"SR. {datos.get('nombre_comprador', '').upper()}", 0, 1, "C")

    # Testigos
    pdf.ln(10)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 6, "TESTIGOS QUE DAN FE", ln=1, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "_________________________________", 0, 0, "C")
    pdf.cell(0, 6, "_________________________________", 0, 1, "C")

    pdf.set_font("Arial", "B", 11)
    pdf.cell(90, 6, f"C. {datos.get('nombre_testigo1', '').upper()}", 0, 0, "C")
    pdf.cell(0, 6, f"C. {datos.get('nombre_testigo2', '').upper()}", 0, 1, "C")

    # Espacio para separación vertical
    pdf.ln(40)

    # Autoridades Ejidales
    pdf.set_font("Arial", "", 11)
    pdf.multi_cell(0, 6, "UNA VEZ RATIFICADO EL DOCUMENTO CON SUS RESPECTIVAS MEDIDAS Y COLINDANCIAS, "
                        "LOS REPRESENTANTES DEL ORGANO EJIDAL, CERTIFICAN EL PRESENTE DOCUMENTO.", align="J")
    pdf.ln(5)

    # Cargos
    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "PDTE. DEL COMISARIADO EJIDAL", 0, 0, "C")
    pdf.cell(0, 6, "PDTE. DEL CONSEJO DE VIGILANCIA", 0, 1, "C")

    # Líneas de firma
    pdf.cell(90, 6, "_________________________________", 0, 0, "C")
    pdf.cell(0, 6, "_________________________________", 0, 1, "C")

    # Nombres de representantes
    pdf.set_font("Arial", "B", 11)
    pdf.cell(90, 6, "C. " + datos.get("presidente_comisariado", "____________________________").upper(), 0, 0, "C")
    pdf.cell(0, 6, "C. " + datos.get("presidente_consejo", "____________________________").upper(), 0, 1, "C")

    pdf.ln(10)

    # Secretario y Tesorero
    pdf.set_font("Arial", "", 11)
    pdf.cell(90, 6, "SECRETARIO", 0, 0, "C")
    pdf.cell(0, 6, "TESORERO", 0, 1, "C")

    pdf.cell(90, 6, "_________________________________", 0, 0, "C")
    pdf.cell(0, 6, "_________________________________", 0, 1, "C")

    pdf.set_font("Arial", "B", 11)
    pdf.cell(90, 6, "C. " + datos.get("secretario", "____________________________").upper(), 0, 0, "C")
    pdf.cell(0, 6, "C. " + datos.get("tesorero", "____________________________").upper(), 0, 1, "C")

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp.name)
    return tmp.name

from flask import Blueprint, render_template, request, redirect, url_for, flash
from tienda.services.producto_service import ProductoService
from tienda.exceptions import ErrorValidacion
 
producto_bp = Blueprint("productos", __name__, url_prefix="/productos")
servicio = ProductoService()
 
@producto_bp.route("/")
def listar():
    productos = servicio.listar_productos()
    return render_template("productos/lista.html", productos=productos)
 
@producto_bp.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        try:
            servicio.crear_producto(
                nombre=request.form.get("nombre", ""),
                precio=request.form.get("precio", "")
            )
            flash("Producto agregado correctamente", "ok")
            return redirect(url_for("productos.listar"))
        except ErrorValidacion as e:
            flash(str(e), "error")
    return render_template("productos/formulario.html")

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify
)

from tienda.services.producto_service import ProductoService
from tienda.exceptions import ErrorValidacion


producto_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos"
)

servicio = ProductoService()


@producto_bp.route("/")
def listar():

    productos = servicio.listar_productos()

    return render_template(
        "productos/lista.html",
        productos=productos
    )


@producto_bp.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":

        try:

            servicio.crear_producto(
                nombre=request.form.get("nombre", ""),
                precio=request.form.get("precio", "")
            )

            flash(
                "Producto agregado correctamente",
                "ok"
            )

            return redirect(
                url_for("productos.listar")
            )

        except ErrorValidacion as e:

            flash(str(e), "error")

    return render_template(
        "productos/formulario.html"
    )


@producto_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    producto = servicio._repo.obtener(id)

    if request.method == "POST":

        try:

            servicio.actualizar_producto(
                id=id,
                nombre=request.form.get("nombre", ""),
                precio=request.form.get("precio", "")
            )

            flash("Producto actualizado", "ok")

            return redirect(
                url_for("productos.listar")
            )

        except ErrorValidacion as e:

            flash(str(e), "error")

    return render_template(
        "productos/editar.html",
        producto=producto
    )


@producto_bp.route("/eliminar/<int:id>")
def eliminar(id):

    servicio.eliminar_producto(id)

    flash("Producto eliminado", "ok")

    return redirect(
        url_for("productos.listar")
    )


# NUEVO ENDPOINT API JSON

@producto_bp.route("/api/productos")
def api_productos():

    productos = servicio.listar_productos()

    return jsonify(
        [p.to_dict() for p in productos]
    )
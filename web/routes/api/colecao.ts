import app = require('teem');
import Colecao = require("../../models/colecao");

class ColecaoApiRoute {
	public async listar(req: app.Request, res: app.Response) {
		res.json(await Colecao.listar());
	}

	public async listarPosicaoPorData(req: app.Request, res: app.Response) {
		res.json(await Colecao.listarPosicaoPorData(parseInt(req.query["id"] as string), req.query["dataInicial"] as string, req.query["dataFinal"] as string));
	}

	public async listarTop10PorData(req: app.Request, res: app.Response) {
		res.json(await Colecao.listarTop10PorData(req.query["data"] as string));
	}
}

export = ColecaoApiRoute;

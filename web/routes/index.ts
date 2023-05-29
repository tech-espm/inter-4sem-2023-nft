import app = require('teem');

class IndexRoute {
	public async index(req: app.Request, res: app.Response) {
		/*
		let dados: any[];

		await app.sql.connect(async (sql) => {

			// Todas os comandos SQL devem ser executados aqui dentro do app.sql.connect().

			dados = await sql.query("SELECT ...");

		});

		let opcoes = {
			dados: dados
		};
		*/

		let opcoes = {
			dados: [],
		};

		res.render('index/index', opcoes);
	}

	public async sobre(req: app.Request, res: app.Response) {
		res.render('index/sobre');
	}
}

export = IndexRoute;

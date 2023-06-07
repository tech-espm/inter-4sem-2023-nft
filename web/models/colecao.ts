import app = require("teem");
import DataUtil = require("../utils/dataUtil");

class Colecao {
	public static async listar(): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query("select id, name, image from collection order by name asc");
		});
	}

	public static async listarPosicaoPorData(id: number, dataInicial: string, dataFinal: string): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query(`
				select date_format(date, '%d/%m/%y') date, ranking
				from dailyreport
				where collection_id = ? and date between ? and ?
				order by date asc
			`, [id, DataUtil.converterDataISO(dataInicial), DataUtil.converterDataISO(dataFinal)]);
		});
	}

	public static async listarTop10(): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query(`
			SELECT collection.name, collection.image, AVG(dailyReport.ranking) AS average_ranking, AVG(floorSale) as avg_floorSale
				FROM collection
				JOIN dailyReport ON collection.id = dailyReport.collection_id
				GROUP BY collection.id, collection.name
				ORDER BY average_ranking ASC
				LIMIT 10;
			`);
		});
	}

	public static async listarTop10PorData(data: string): Promise<any[]> {
		return app.sql.connect(async (sql) => {
			return sql.query(`
			select dr.ranking, c.id, c.name, c.image
				from dailyreport dr
				inner join collection c on c.id = dr.collection_id
				where dr.date = ? and dr.ranking <= 10
				order by dr.ranking;
			`, [DataUtil.converterDataISO(data)]);
		});
	}
}

export = Colecao;

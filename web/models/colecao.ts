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
			SELECT c.name, c.image, ROUND(AVG(dr.ranking),1) AS avg_ranking, AVG(dr.floorSale) as avg_floorSale, AVG(dr.volumeChange) as avg_volumeChange, ROUND(AVG(dr.ownerCount),0) as avg_ownerCount, ROUND(AVG(dr.tokenCount),0) as avg_tokenCount, ROUND(AVG(onSaleCount),0) as avg_onSaleCount
				FROM collection c
				JOIN dailyReport dr ON c.id = dr.collection_id
				GROUP BY c.id, c.name
				ORDER BY avg_ranking ASC
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

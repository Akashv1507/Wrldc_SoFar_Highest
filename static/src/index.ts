import { getSoFarHighestData } from "./fetchDataApi";
import { appConfig } from "./config";
// declare var $:any;

export interface RespObj {
  metricName: string;
  soFarHighest: number;
  soFarHighestTimestamp: string;
  prevSoFarHighest: number;
  prevSoFarHighestTimestamp: string;
}
export interface DataFromApi {
  respData: RespObj;
}

interface Accumulator {
  accumulatorList: RespObj[];
}

let intervalID = null;
window.onload = async () => {
  intervalID = setInterval(refreshData, 1000 * 60 * 30);
  (document.getElementById("refreshBtn") as HTMLButtonElement).onclick =
    refreshData;
  refreshData();
};

const refreshData = async () => {
  // iterating through each tableId in appConfig
  for (let tableInd = 0; tableInd < appConfig.length; tableInd++) {
    // accumulator for all the metrices for a single table
    let accumulator: Accumulator = { accumulatorList: [] };

    // iterating through each metricId corresponidng to a table
    for (
      let metricInd = 0;
      metricInd < appConfig[tableInd]["metricNames"].length;
      metricInd++
    ) {
      let fetchedData = await getSoFarHighestData(
        appConfig[tableInd]["dataSource"],
        appConfig[tableInd]["metricNames"][metricInd]
      );

      accumulator.accumulatorList.push(fetchedData["respData"]);
    }
    console.log(accumulator);
    $(`#${appConfig[tableInd]["tblId"]}`).DataTable().destroy();
    $(`#${appConfig[tableInd]["tblId"]}`).DataTable({
      dom: "",
      data: accumulator.accumulatorList,
      columns: [
        { data: "metricName", title: "Metric Name" },
        { data: "soFarHighest", title: "Highest" },
        { data: "soFarHighestTimestamp", title: "Time Highest" },
        { data: "prevSoFarHighest", title: "Prev Highest" },
        { data: "prevSoFarHighestTimestamp", title: "Time Prev Highest" },
      ],
    });
  }
};

export const appConfig = [
  {
    tblId: "demand_tbl",
    metrics: [
      {
        metricName: "WR_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "WR-Demand(MW)",
      },
      {
        metricName: "MAH_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "Maharashtra-Demand(MW)",
      },
      {
        metricName: "GUJ_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "Gujarat-Demand(MW)",
      },
      {
        metricName: "MP_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "MP-Demand(MW)",
      },
      {
        metricName: "CHATT_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "Chhattisgarh-Demand(MW)",
      },
      {
        metricName: "GOA_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "Goa-Demand(MW)",
      },
      {
        metricName: "DD_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "DD-Demand(MW)",
      },
      {
        metricName: "DNH_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "DNH-Demand(MW)",
      },
      {
        metricName: "AMNSIL_DEM_MW",
        dataSource: "SCADA_API",
        displayName: "Amnsil-Demand(MW)",
      },
    ],
  },
  {
    tblId: "energy_consumption_tbl",
    metrics: [
      {
        metricName: "WR_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "WR-Demand(MU)",
      },
      {
        metricName: "MAH_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "Maharashtra-Demand(MU)",
      },
      {
        metricName: "GUJ_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "Gujarat-Demand(MU)",
      },
      {
        metricName: "MP_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "MP-Demand(MU)",
      },
      {
        metricName: "CHATT_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "Chhattisgarh-Demand(MU)",
      },
      {
        metricName: "GOA_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "Goa-Demand(MU)",
      },
      {
        metricName: "DD_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "DD-Demand(MU)",
      },
      {
        metricName: "DNH_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "DNH-Demand(MU)",
      },
      {
        metricName: "AMNSIL_DEM_MU",
        dataSource: "PSP_DB",
        displayName: "Amnsil-Demand(MU)",
      },
    ],
  },
  {
    tblId: "wind_gen_mw_tbl",
    metrics: [
      {
        metricName: "GUJ_WIND_MW",
        dataSource: "SCADA_API",
        displayName: "Gujarat-Wind(MW)",
      },
      {
        metricName: "MAH_WIND_MW",
        dataSource: "SCADA_API",
        displayName: "Maharashtra-Wind(MW)",
      },
      {
        metricName: "MP_WIND_MW",
        dataSource: "SCADA_API",
        displayName: "MP-Wind(MW)",
      },
      {
        metricName: "CENTRAL_WIND_MW",
        dataSource: "SCADA_API",
        displayName: "ISTS_Wind(MW)",
      },
      {
        metricName: "WR_WIND_MW",
        dataSource: "SCADA_API",
        displayName: "WR_Wind(MW)",
      },
    ],
  },
  {
    tblId: "wind_gen_mu_tbl",
    metrics: [
      {
        metricName: "GUJ_WIND_MU",
        dataSource: "PSP_DB",
        displayName: "Gujarat-Wind(MU)",
      },
      {
        metricName: "MAH_WIND_MU",
        dataSource: "PSP_DB",
        displayName: "Maharashtra-Wind(MU)",
      },
      {
        metricName: "MP_WIND_MU",
        dataSource: "PSP_DB",
        displayName: "MP-Wind(MU)",
      },
      {
        metricName: "CENTRAL_WIND_MU",
        dataSource: "PSP_DB",
        displayName: "ISTS_Wind(MU)",
      },
      {
        metricName: "WR_WIND_MU",
        dataSource: "PSP_DB",
        displayName: "WR_Wind(MU)",
      },
    ],
  },
  {
    tblId: "solar_gen_mw_tbl",
    metrics: [
      {
        metricName: "GUJ_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "Gujarat-Solar(MW)",
      },
      {
        metricName: "MAH_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "Maharashtra-Solar(MW)",
      },
      {
        metricName: "MP_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "MP-Solar(MW)",
      },
      {
        metricName: "CHATT_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "Chhattisgarh-Solar(MW)",
      },
      {
        metricName: "CENTRAL_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "ISTS-Solar(MW)",
      },
      {
        metricName: "WR_SOLAR_MW",
        dataSource: "SCADA_API",
        displayName: "WR-Solar(MW)",
      },
    ],
  },
  {
    tblId: "solar_gen_mu_tbl",
    metrics: [
      {
        metricName: "GUJ_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "Gujarat-Solar(MW)",
      },
      {
        metricName: "MAH_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "Maharashtra-Solar(MU)",
      },
      {
        metricName: "MP_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "MP-Solar(MU)",
      },
      {
        metricName: "CHATT_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "Chhattisgarh-Solar(MU)",
      },
      {
        metricName: "CENTRA_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "ISTS-Solar(MU)",
      },
      {
        metricName: "WR_SOLAR_MU",
        dataSource: "PSP_DB",
        displayName: "WR-Solar(MU)",
      },
    ],
  },
  {
    tblId: "re_comb_mw_tbl",
    metrics: [
      {
        metricName: "GUJ_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "Gujarat-RE-Comb(MW)",
      },
      {
        metricName: "MAH_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "Maharashtra-RE-Comb(MW)",
      },
      {
        metricName: "MP_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "MP-RE-Comb(MW)",
      },
      {
        metricName: "CHATT_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "Chhattisgarh-RE-Comb(MW)",
      },
      {
        metricName: "CENTRAL_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "ISTS-RE-Comb(MW)",
      },
      {
        metricName: "WR_RE_COMB_MW",
        dataSource: "SCADA_API",
        displayName: "WR-RE-Comb(MW)",
      },
    ],
  },
  {
    tblId: "re_comb_mu_tbl",
    metrics: [
      {
        metricName: "GUJ_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "Gujarat-RE-Comb(MU)",
      },
      {
        metricName: "MAH_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "Maharashtra-RE-Comb(MU)",
      },
      {
        metricName: "MP_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "MP-RE-Comb(MU)",
      },
      {
        metricName: "CHATT_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "Chhattisgarh-RE-Comb(MU)",
      },
      {
        metricName: "CENTRAL_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "ISTS-RE-Comb(MU)",
      },
      {
        metricName: "WR_RE_COMB_MU",
        dataSource: "PSP_DB",
        displayName: "WR-RE-Comb(MU)",
      },
    ],
  },
];

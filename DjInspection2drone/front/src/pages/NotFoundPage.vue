import Vue from 'vue';
import { AgGridVue } from '@ag-grid-community/vue';
import { AllCommunityModules } from '@ag-grid-community/all-modules';
import '@ag-grid-community/all-modules/dist/styles/ag-grid.css';
import '@ag-grid-community/all-modules/dist/styles/ag-theme-alpine.css';
import ChildMessageRenderer from './childMessageRendererVue.js';
import CubeRenderer from './cubeRendererVue.js';
import CurrencyRenderer from './currencyRendererVue.js';
import ParamsRenderer from './paramsRendererVue.js';
import SquareRenderer from './squareRendererVue.js';

const VueExample = {
  template: `
        <div style="height: 100%">
            <button v-on:click="refreshEvenRowsCurrencyData()" style="margin-bottom: 10px" class="btn btn-primary">
                Refresh Even Row Currency Data
            </button>
            <div style="height: calc(100% - 55px);">
                <ag-grid-vue
                style="width: 100%; height: 100%;"
                class="ag-theme-alpine"
                id="myGrid"
                :gridOptions="gridOptions"
                @grid-ready="onGridReady"
                :columnDefs="columnDefs"
                :rowData="rowData"
                :context="context"
                :frameworkComponents="frameworkComponents"
                :defaultColDef="defaultColDef"
                :modules="modules"></ag-grid-vue>
            </div>
        </div>
    `,
  components: {
    'ag-grid-vue': AgGridVue,
  },
  data: function() {
    return {
      gridOptions: null,
      gridApi: null,
      columnApi: null,
      columnDefs: null,
      rowData: null,
      context: null,
      frameworkComponents: null,
      defaultColDef: null,
      modules: AllCommunityModules,
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {
        headerName: 'Row',
        field: 'row',
        width: 150,
      },
      {
        headerName: 'Square',
        field: 'value',
        cellRenderer: 'squareRenderer',
        editable: true,
        colId: 'square',
        width: 150,
      },
      {
        headerName: 'Cube',
        field: 'value',
        cellRenderer: 'cubeRenderer',
        colId: 'cube',
        width: 150,
      },
      {
        headerName: 'Row Params',
        field: 'row',
        cellRenderer: 'paramsRenderer',
        colId: 'params',
        width: 150,
      },
      {
        headerName: 'Currency (Pipe)',
        field: 'currency',
        cellRenderer: 'currencyRenderer',
        colId: 'currency',
        width: 120,
      },
      {
        headerName: 'Child/Parent',
        field: 'value',
        cellRenderer: 'childMessageRenderer',
        colId: 'params',
        width: 180,
      },
    ];
    this.rowData = createRowData();
    this.context = { componentParent: this };
    this.frameworkComponents = {
      squareRenderer: SquareRenderer,
      cubeRenderer: CubeRenderer,
      paramsRenderer: ParamsRenderer,
      currencyRenderer: CurrencyRenderer,
      childMessageRenderer: ChildMessageRenderer,
    };
    this.defaultColDef = {
      editable: true,
      sortable: true,
      flex: 1,
      minWidth: 100,
      filter: true,
      resizable: true,
    };
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
  },
  methods: {
    refreshEvenRowsCurrencyData() {
      this.gridApi.forEachNode(function(rowNode) {
        if (rowNode.data.value % 2 === 0) {
          rowNode.setDataValue(
            'currency',
            rowNode.data.value + Number(Math.random().toFixed(2))
          );
        }
      });
      this.gridApi.refreshCells({ columns: ['currency'] });
    },
    on
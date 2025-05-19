<template>
<div>
    <h2>Cantidad de las solicitudes realizadas agrupadas por estado</h2>
    <div ref="chart"></div>
    <div class="legend"></div>
</div>
</template>

<script>
import * as d3 from 'd3';
import { apiService } from '../services/api';

export default {
data() {
    return {
    chartData: [],
    };
},
mounted() {
    this.fetchChartData();
},
methods: {
    fetchChartData() {
    apiService.get('/api/data/status-pie-chart')
        .then(response => {
        this.chartData = response.data;
        this.createChart();
        })
        .catch(error => {
        console.error('Error al cargar datos', error);
        });
    },
    createChart() {
    if (!this.chartData || this.chartData.length === 0) {
        console.error('No hay datos para el gráfico');
        return;
    }

    const width = 300;
    const height = 300;
    const radius = Math.min(width, height) / 2 - 10;

    const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2},${height / 2})`);

    // Paleta de colores personalizada
    const color = d3.scaleOrdinal(['#4e79a7', '#f28e2b', '#e15759', '#76b7b2', '#59a14f']);

    const pie = d3.pie().value(d => d.count);
    const arc = d3.arc().innerRadius(0).outerRadius(radius);

    const arcs = svg.selectAll('path')
        .data(pie(this.chartData))
        .join('path')
        .attr('fill', (d, i) => color(i))
        .attr('d', arc)
        .append('title')
        .text(d => `${d.data.status}: ${d.data.count}`);

    arcs.append('text')
        .attr('transform', d => `translate(${arc.centroid(d)})`)
        .attr('text-anchor', 'middle')
        .attr('alignment-baseline', 'middle')
        .style('fill', 'white')  // Color del texto
        .style('font-size', '12px')  // Tamaño de fuente
        .style('font-weight', 'bold')  // Peso de la fuente
        .text(d => d.data.count.toLocaleString('en-US'));

    // Agregar una leyenda
    const legend = d3.select('.legend')
        .append('svg')
        .attr('width', 120)
        .attr('height', this.chartData.length * 20);

    const legendItems = legend.selectAll('.legend-item')
        .data(this.chartData.map(d => d.status))
        .enter()
        .append('g')
        .attr('class', 'legend-item')
        .attr('transform', (d, i) => `translate(0, ${i * 20})`);

    legendItems.append('rect')
        .attr('width', 18)
        .attr('height', 18)
        .attr('fill', (d, i) => color(i));

    legendItems.append('text')
        .attr('x', 24)
        .attr('y', 9)
        .attr('dy', '.35em')
        .style('font-size', '12px')
        .text(d => d);
    },
},
};
</script>

<style scoped>
/* Estilos específicos del componente si es necesario */
</style>
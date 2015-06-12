import list_view
import pipeline_view
import nested_view
import sectioned_view

converters = {
    'list': list_view.convert_to_xml,
    'pipeline': pipeline_view.convert_to_xml,
    'nested': nested_view.convert_to_xml,
    'sectioned': sectioned_view.convert_to_xml
}

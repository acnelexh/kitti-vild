from pathlib import Path
import pdb

#hard code
SAVE_PATH = Path("./")

def write_result(outputs, threshold = 0.5):
    '''
    outputs_key = ['pred_image_info',
        'pred_num_detections',
        'pred_detection_boxes',
        'pred_detection_classes',
        'pred_detection_scores',
        'pred_detection_masks',
        'pred_source_id',
        'gt_source_id',
        'gt_height',
        'gt_width',
        'gt_image_info',
        'gt_num_detections',
        'gt_boxes',
        'gt_classes',
        'gt_areas',
        'gt_is_crowds']
    '''
    look_up = {
        1: "cyclist",
        2: "pedestrian",
        3: "car",
        4: "tram",
        5: "truck",
        6: "van",
        7: "misc"
    }
    source_id = outputs['pred_source_id']
    pred_boxes = outputs['pred_detection_boxes']
    pred_classes = outputs['pred_detection_classes']
    pred_scores = outputs['pred_detection_scores']
    
    for idx, i in enumerate(source_id):
        writename = str(i).zfill(6) + ".txt"
        scores_i = pred_scores[idx]
        classes_i = pred_classes[idx][scores_i > 0.5]
        boxes_i = pred_boxes[idx][scores_i > 0.5]
        scores_i = pred_scores[idx][scores_i > 0.5]
        
        with open(SAVE_PATH/writename, 'w') as o:
            for obj, c in enumerate(classes_i):
                xmin, ymin, xmax, ymax = [float(x) for x in boxes_i[obj]]
                write_line = f"{look_up[c]} {-1} {-1} {-10} {xmin:.2f} {ymin:.2f} {xmax:.2f} {ymax:.2f} {-1} {-1} {-1} {-1000} {-1000} {-1000} {-10} {scores_i[obj]:.4f}"
                o.write(write_line + '\n')
    
            
        
    
    